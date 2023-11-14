"""
Test schema operations
"""

import os
import shutil
import unittest
from io import BytesIO
from pathlib import Path
from unittest import mock

import requests_mock

from nshm_toshi_client.toshi_client_base import clean_string
from nshm_toshi_client.toshi_file import ToshiFile

API_URL = "http://fake_api/graphql"
S3_URL = "https://some-tosh-api.com/"


class TestToshiFile(unittest.TestCase):
    def test_create_toshi_file_ok(self):
        with requests_mock.Mocker() as m:

            post_url = clean_string('{"acl": "public-read", "Content-MD5": "VXFQl5qqeuR/f4Yr4N0yQg=="}')

            query1_server_answer = '{"data":{"create_file":{"file_result":{"id":"ABCD","post_url":"%s"}}}}' % post_url

            m.post(API_URL, text=query1_server_answer)
            headers = {"x-api-key": "THE_API_KEY"}
            myapi = ToshiFile(API_URL, S3_URL, None, with_schema_validation=False, headers=headers)

            filepath = Path(__file__)
            _id, post_url = myapi.create_file(filepath)

            assert post_url["Content-MD5"] == "VXFQl5qqeuR/f4Yr4N0yQg=="

            history = m.request_history
            # print('HIST', history[0].text)
            assert history[0].url == API_URL

    def test_create_toshi_file_with_meta_ok(self):
        with requests_mock.Mocker() as m:

            post_url = clean_string('{"acl": "public-read", "Content-MD5": "VXFQl5qqeuR/f4Yr4N0yQg=="}')

            query1_server_answer = '{"data":{"create_file":{"file_result":{"id":"ABCD","post_url":"%s"}}}}' % post_url

            m.post(API_URL, text=query1_server_answer)
            headers = {"x-api-key": "THE_API_KEY"}
            myapi = ToshiFile(API_URL, S3_URL, None, with_schema_validation=False, headers=headers)

            meta = dict(mykey="myvalue", mykey2='myothervalue')

            filepath = Path(__file__)
            _id, post_url = myapi.create_file(filepath, meta)

            assert post_url["Content-MD5"] == "VXFQl5qqeuR/f4Yr4N0yQg=="

            history = m.request_history
            # print('HIST', history[0].text)
            assert history[0].url == API_URL

    def test_get_file_ok(self):
        with requests_mock.Mocker() as m:

            query1_server_answer = '''{
                "data": {
                    "node": {
                        "__typename": "InversionSolutionNrml",
                        "id": "SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw==",
                        "file_name": "NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip",
                        "file_size": 3331426,
                        "meta": {"mykey":"myvalue","mykey2":"myothervalue"}
                    }
                }
            }'''

            m.post(API_URL, text=query1_server_answer)
            headers = {"x-api-key": "THE_API_KEY"}
            myapi = ToshiFile(API_URL, S3_URL, None, with_schema_validation=False, headers=headers)

            file_detail = myapi.get_file("SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw==")

            assert file_detail["id"] == "SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw=="
            assert file_detail["file_name"] == "NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip"
            assert file_detail["file_size"] == 3331426
            assert file_detail["meta"] == {"mykey": "myvalue", "mykey2": "myothervalue"}

    def test_get_file_dowload_url_ok(self):
        with requests_mock.Mocker() as m:

            query1_server_answer = '''{
                "data": {
                    "node": {
                        "__typename": "InversionSolutionNrml",
                        "id": "SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw==",
                        "file_name": "NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip",
                        "file_size": 3331426,
                        "meta": {"mykey":"myvalue","mykey2":"myothervalue"},
                        "file_url": "https://somewhere/ABC-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip"
                    }
                }
            }'''

            m.post(API_URL, text=query1_server_answer)
            headers = {"x-api-key": "THE_API_KEY"}
            myapi = ToshiFile(API_URL, S3_URL, None, with_schema_validation=False, headers=headers)

            file_detail = myapi.get_file("SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw==", True)

            assert file_detail["id"] == "SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw=="
            assert file_detail["file_name"] == "NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip"
            assert file_detail["file_size"] == 3331426
            assert file_detail["meta"] == {"mykey": "myvalue", "mykey2": "myothervalue"}
            assert file_detail["file_url"] == "https://somewhere/ABC-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip"

    def mocked_requests_get(*args, **kwargs):
        with open(Path(__file__).parent / "test_data" / "sample.zip", "rb") as f:
            mock_zip = BytesIO(f.read())
            mock_zip.seek(0)

        class MockResponse:
            def __init__(self, json_data, status_code, ok):
                self.json = json_data
                self.status_code = status_code
                self.ok = ok
                self.content = mock_zip.read()

        if args[0] == 'https://somewhere/ABC-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip':
            return MockResponse({"key1": "value1"}, 200, True)
        else:
            return MockResponse(None, 404, False)

    @mock.patch('nshm_toshi_client.toshi_file.requests.get', side_effect=mocked_requests_get)
    def test_download_file_ok(self, mock_get):
        with requests_mock.Mocker() as m:

            query1_server_answer = '''{
                "data": {
                    "node": {
                        "__typename": "InversionSolutionNrml",
                        "id": "SW52ZXJzaW9uU29sdXRpb25Ocm1sOjEwMDM0Mw==",
                        "file_name": "NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip",
                        "file_url": "https://somewhere/ABC-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip"
                    }
                }
            }'''

            m.post(API_URL, text=query1_server_answer)
            headers = {"x-api-key": "THE_API_KEY"}
            myapi = ToshiFile(API_URL, S3_URL, None, with_schema_validation=False, headers=headers)

            dir_path = os.path.abspath(os.getcwd())
            file_path = os.path.join(dir_path, "tmp")

            myapi.download_file(
                "https://somewhere/ABC-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip",
                file_path,
            )

            assert os.path.exists(f"{file_path}/NZSHM22_InversionSolution-QXV0b21hdGlvblRhc2s6MTAwMTA4_nrml.zip")

    def tearDown(self) -> None:
        tmp_dir = os.path.join(os.path.abspath(os.getcwd()), "tmp")
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)
