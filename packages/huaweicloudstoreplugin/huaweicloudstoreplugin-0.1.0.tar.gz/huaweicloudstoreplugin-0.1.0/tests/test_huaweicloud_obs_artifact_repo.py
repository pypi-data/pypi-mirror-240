# pylint: disable=redefined-outer-name
import os
import mock
import pytest

from obs.bucket import BucketClient
from obs.model import GetResult, ListObjectsResponse, Content, CommonPrefix, ObjectStream, PutContentResponse

from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository
from huaweicloudstoreplugin.store.artifact.huaweicloud_obs_artifact_repo import HuaweiCloudObsArtifactRepository


@pytest.fixture
def obs_bucket_mock():
    # Make sure that our environment variable aren't set to actually access Huawei Cloud
    old_region = os.environ.get('MLFLOW_OBS_REGION')
    old_obs_access_key_id = os.environ.get('MLFLOW_OBS_ACCESS_KEY_ID')
    old_obs_secret_access_key = os.environ.get('MLFLOW_OBS_SECRET_ACCESS_KEY')
    if old_region is not None:
        del os.environ['MLFLOW_OBS_REGION']
    if old_obs_access_key_id is not None:
        del os.environ['MLFLOW_OBS_ACCESS_KEY_ID']
    if old_obs_secret_access_key is not None:
        del os.environ['MLFLOW_OBS_SECRET_ACCESS_KEY']
    bucket_client = mock.MagicMock(autospec=BucketClient)
    body = ListObjectsResponse(contents=[])
    bucket_client.return_value.putFile.return_value = GetResult(status=200, reason='OK', body=body)
    bucket_client.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)
    yield bucket_client

    if old_region is not None:
        os.environ['MLFLOW_OBS_REGION'] = old_region
    if old_obs_access_key_id is not None:
        os.environ['MLFLOW_OBS_ACCESS_KEY_ID'] = old_obs_access_key_id
    if old_obs_secret_access_key is not None:
        os.environ['MLFLOW_OBS_SECRET_ACCESS_KEY'] = old_obs_secret_access_key


def test_artifact_uri_factory(obs_bucket_mock):
    # pylint: disable=unused-argument
    # We do need to set up a fake access key for the code to run though
    os.environ['MLFLOW_OBS_REGION'] = 'temp_MLFLOW_OBS_REGION'
    os.environ['MLFLOW_OBS_ACCESS_KEY_ID'] = 'temp_MLFLOW_OBS_ACCESS_KEY_ID'
    os.environ['MLFLOW_OBS_SECRET_ACCESS_KEY'] = 'temp_MLFLOW_OBS_SECRET_ACCESS_KEY'
    repo = get_artifact_repository("obs://test_bucket/some/path")
    assert isinstance(repo, HuaweiCloudObsArtifactRepository)
    del os.environ['MLFLOW_OBS_REGION']
    del os.environ['MLFLOW_OBS_ACCESS_KEY_ID']
    del os.environ['MLFLOW_OBS_SECRET_ACCESS_KEY']


def test_log_artifact(obs_bucket_mock, tmpdir):
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/some/path", obs_bucket_mock)
    repo._get_bucket_client = obs_bucket_mock
    body = PutContentResponse()
    repo.obs_bucket.return_value.putFile.return_value = GetResult(status=200, reason='OK', body=body)
    tmp_folder = tmpdir.mkdir("data")
    tmp_file = tmp_folder.join("test.txt")
    tmp_file.write("hello world!")
    fpath = tmp_folder + '/test.txt'
    fpath = fpath.strpath
    repo.log_artifact(fpath)

    repo.obs_bucket.return_value.putFile.assert_called_with(objectKey='some/path/test.txt', file_path=fpath)


def test_log_artifacts(obs_bucket_mock, tmpdir):
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/some/path", obs_bucket_mock)
    repo._get_bucket_client = obs_bucket_mock

    tmp_folder = tmpdir.mkdir("data")
    tmp_folder.mkdir('aa').join('a.txt').write('aa')
    tmp_folder.mkdir('bb').join('b.txt').write('bb')
    tmp_folder.mkdir('cc').join('c.txt').write('cc')
    body = PutContentResponse()
    repo.obs_bucket.return_value.putFile.return_value = [
        ('some/path/data/aa', [('some/path/data/aa/a.txt', GetResult(status=200, reason='OK', body=body))]),
        ('some/path/data/bb', [('some/path/data/bb/b.txt', GetResult(status=200, reason='OK', body=body))]),
        ('some/path/data/cc', [('some/path/data/cc/c.txt', GetResult(status=200, reason='OK', body=body))]),
    ]

    repo.log_artifacts(tmp_folder.strpath, 'data')

    repo.obs_bucket.return_value.putFile.assert_called_with(objectKey='some/path/data', file_path=tmp_folder.strpath)


def test_list_artifacts_empty(obs_bucket_mock):
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/some/path", obs_bucket_mock)
    repo._get_bucket_client = repo.obs_bucket

    body = ListObjectsResponse(contents=[], commonPrefixs=[])
    repo.obs_bucket.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)

    assert repo.list_artifacts() == []


def test_list_artifacts(obs_bucket_mock):
    artifact_root_path = "experiment_id/run_id/"
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/" + artifact_root_path, obs_bucket_mock)
    repo._get_bucket_client = obs_bucket_mock
    file_path = 'file'
    dir_name = "model"
    dir_path = artifact_root_path + dir_name + "/"

    content = Content(
        key=artifact_root_path + file_path,
        lastModified='2023/03/02 16:43:49',
        size=1,
        etag=None,
        owner=None,
        storageClass=None,
        isAppendable=False
    )
    prefix = CommonPrefix(prefix=dir_path)
    body = ListObjectsResponse(contents=[content], commonPrefixs=[prefix])
    repo.obs_bucket.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)

    artifacts = repo.list_artifacts(path=None)

    assert len(artifacts) == 2
    assert artifacts[0].path == file_path
    assert artifacts[0].is_dir is False
    assert artifacts[0].file_size == content.size
    assert artifacts[1].path == dir_name
    assert artifacts[1].is_dir is True
    assert artifacts[1].file_size is None


def test_list_artifacts_with_subdir(obs_bucket_mock):
    artifact_root_path = "experiment_id/run_id/"
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/" + artifact_root_path, obs_bucket_mock)
    repo._get_bucket_client = repo.obs_bucket
    # list artifacts at sub directory level
    dir_name = "model"
    file_path = dir_name + "/" + 'model.pb'
    subdir_name = dir_name + "/" + 'variables'
    subdir_path = artifact_root_path + subdir_name + "/"

    content = Content(
        key=artifact_root_path + file_path,
        lastModified='2023/03/02 16:43:49',
        size=1,
        etag=None,
        owner=None,
        storageClass=None,
        isAppendable=False
    )
    prefix = CommonPrefix(prefix=subdir_path)
    body = ListObjectsResponse(contents=[content], commonPrefixs=[prefix])
    repo.obs_bucket.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)

    artifacts = repo.list_artifacts(path=dir_name)
    assert len(artifacts) == 2
    assert artifacts[0].path == file_path
    assert artifacts[0].is_dir is False
    assert artifacts[0].file_size == content.size
    assert artifacts[1].path == subdir_name
    assert artifacts[1].is_dir is True
    assert artifacts[1].file_size is None


def test_download_file_artifact(obs_bucket_mock, tmpdir):
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/some/path", obs_bucket_mock)
    repo._get_bucket_client = repo.obs_bucket

    tmp_file_name = 'temp.txt'
    tmp_file_content = "test content"

    tmpdir.join(tmp_file_name).write(tmp_file_content)

    local_path = os.path.join(tmpdir, tmp_file_name)
    body = ListObjectsResponse(contents=[], commonPrefixs=[])
    repo.obs_bucket.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)
    body = ObjectStream(url=local_path)
    repo.obs_bucket.return_value.getObject.return_value = GetResult(status=200, reason='OK', body=body)

    repo.log_artifact(local_path)

    download_file_path = repo.download_artifacts(tmp_file_name, dst_path=tmpdir)
    with open(download_file_path, 'r') as rf:
        assert rf.read() == tmp_file_content


def test_delete_artifacts(obs_bucket_mock, tmpdir):
    repo = HuaweiCloudObsArtifactRepository("obs://test_bucket/some/path", obs_bucket_mock)
    repo._get_bucket_client = repo.obs_bucket

    subdir = tmpdir.mkdir('subdir')
    nested = subdir.mkdir('nested')

    subdir_path = subdir.strpath
    nested_path = nested.strpath
    print('subdir_path: ', subdir_path)
    print('nested_path: ', nested_path)

    subdir.join('a.txt').write('A')
    subdir.join('b.txt').write('B')
    nested.join('c.txt').write('C')

    contents = [
        Content(key='some/path/a.txt'),
        Content(key='some/path/b.txt'),
        Content(key='some/path/nested/'),
        Content(key='some/path/nested/c.txt'),
    ]
    body = ListObjectsResponse(contents=contents, commonPrefixs=[])
    repo.obs_bucket.return_value.listObjects.return_value = GetResult(status=200, reason='OK', body=body)
    repo.obs_bucket.return_value.deleteObject.return_value = GetResult(status=204, reason='No Content', body={})
    repo.log_artifacts(subdir_path)

    # confirm that artifacts are present
    artifact_file_names = [obj.path for obj in repo.list_artifacts()]
    assert "a.txt" in artifact_file_names
    assert "b.txt" in artifact_file_names
    assert "nested" in artifact_file_names

    repo.delete_artifacts()
    repo.obs_bucket.return_value.deleteObject.assert_has_calls([
        mock.call(objectKey='some/path/a.txt'),
        mock.call(objectKey='some/path/b.txt'),
        mock.call(objectKey='some/path/nested/'),
        mock.call(objectKey='some/path/nested/c.txt'),
    ], any_order=True)

