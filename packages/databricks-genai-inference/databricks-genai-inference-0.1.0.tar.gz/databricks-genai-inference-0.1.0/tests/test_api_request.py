from unittest.mock import patch

import pytest
from constants import (CHAT_COMPLETION_MESSAGES, CHAT_COMPLETION_MODEL_NAME, COMPLETION_MODEL_NAME, COMPLETION_PROMPT_1,
                       COMPLETION_PROMPT_2, EMBEDDING_INPUT_1, EMBEDDING_INPUT_2, EMBEDDING_INSTRUCTION,
                       EMBEDDING_MODEL_NAME, TEST_API_KEY, TEST_ECHO, TEST_ERROR_BEHAVIOR, TEST_HOST_NAME,
                       TEST_MAX_TOKENS, TEST_N, TEST_STOP, TEST_SUFFIX, TEST_TEMPERATURE, TEST_TIMEOUT, TEST_TOP_K,
                       TEST_TOP_P, TEST_USE_RAW_PROMPT, TEST_USER)

from databricks_genai_inference import ChatCompletion, Completion, Embedding


class TestAPIRequest:

    # Fixture to change an environment variable temporarily
    @pytest.fixture(autouse=True)
    def mock_env_var(self, monkeypatch):
        monkeypatch.setenv('DATABRICKS_HOST', TEST_HOST_NAME)
        monkeypatch.setenv('DATABRICKS_TOKEN', TEST_API_KEY)

    @patch('databricks_genai_inference.ChatCompletion._get_non_streaming_response')
    def test_chat_completion_request_non_streaming(self, mocked_request):
        kwargs = {
            "model": CHAT_COMPLETION_MODEL_NAME,
            "messages": CHAT_COMPLETION_MESSAGES,
            "temperature": TEST_TEMPERATURE,
            "stop": TEST_STOP,
            "max_tokens": TEST_MAX_TOKENS,
            "top_p": TEST_TOP_P,
            "top_k": TEST_TOP_K,
            "user": TEST_USER,
            "timeout": TEST_TIMEOUT,
            "n": TEST_N,
        }
        expected_request = {
            "url": f'{TEST_HOST_NAME}/serving-endpoints/databricks-{CHAT_COMPLETION_MODEL_NAME}/invocations',
            "headers": {
                'authorization': "Bearer " + TEST_API_KEY,
                'Content-Type': 'application/json'
            },
            "json": {
                "model": CHAT_COMPLETION_MODEL_NAME,
                "messages": CHAT_COMPLETION_MESSAGES,
                "temperature": TEST_TEMPERATURE,
                "stop": TEST_STOP,
                "max_tokens": TEST_MAX_TOKENS,
                "top_p": TEST_TOP_P,
                "top_k": TEST_TOP_K,
                "user": TEST_USER,
                "n": TEST_N,
            },
            "timeout": TEST_TIMEOUT,
        }
        ChatCompletion.create(**kwargs)
        mocked_request.assert_called_once_with(**expected_request)

    @patch('databricks_genai_inference.ChatCompletion._get_streaming_response')
    def test_chat_completion_request_streaming(self, mocked_request):
        kwargs = {
            "model": CHAT_COMPLETION_MODEL_NAME,
            "messages": CHAT_COMPLETION_MESSAGES,
            "temperature": TEST_TEMPERATURE,
            "stop": TEST_STOP,
            "max_tokens": TEST_MAX_TOKENS,
            "top_p": TEST_TOP_P,
            "top_k": TEST_TOP_K,
            "user": TEST_USER,
            "timeout": TEST_TIMEOUT,
            "n": TEST_N,
            "stream": True
        }
        expected_request = {
            "url": f'{TEST_HOST_NAME}/serving-endpoints/databricks-{CHAT_COMPLETION_MODEL_NAME}/invocations',
            "headers": {
                'authorization': "Bearer " + TEST_API_KEY,
                'Content-Type': 'application/json'
            },
            "json": {
                "model": CHAT_COMPLETION_MODEL_NAME,
                "messages": CHAT_COMPLETION_MESSAGES,
                "temperature": TEST_TEMPERATURE,
                "stop": TEST_STOP,
                "max_tokens": TEST_MAX_TOKENS,
                "top_p": TEST_TOP_P,
                "top_k": TEST_TOP_K,
                "user": TEST_USER,
                "n": TEST_N,
                "stream": True
            },
            "timeout": TEST_TIMEOUT,
        }
        ChatCompletion.create(**kwargs)
        mocked_request.assert_called_once_with(**expected_request)

    @patch('databricks_genai_inference.Completion._get_non_streaming_response')
    def test_completion_request_non_streaming(self, mocked_request):
        kwargs = {
            "model": COMPLETION_MODEL_NAME,
            "prompt": [COMPLETION_PROMPT_1, COMPLETION_PROMPT_2],
            "temperature": TEST_TEMPERATURE,
            "stop": TEST_STOP,
            "max_tokens": TEST_MAX_TOKENS,
            "top_p": TEST_TOP_P,
            "top_k": TEST_TOP_K,
            "user": TEST_USER,
            "timeout": TEST_TIMEOUT,
            "n": TEST_N,
            "suffix": TEST_SUFFIX,
            "echo": TEST_ECHO,
            "error_behavior": TEST_ERROR_BEHAVIOR,
            "use_raw_prompt": TEST_USE_RAW_PROMPT,
        }
        expected_request = {
            "url": f'{TEST_HOST_NAME}/serving-endpoints/databricks-{COMPLETION_MODEL_NAME}/invocations',
            "headers": {
                'authorization': "Bearer " + TEST_API_KEY,
                'Content-Type': 'application/json'
            },
            "json": {
                "model": COMPLETION_MODEL_NAME,
                "prompt": [COMPLETION_PROMPT_1, COMPLETION_PROMPT_2],
                "temperature": TEST_TEMPERATURE,
                "stop": TEST_STOP,
                "max_tokens": TEST_MAX_TOKENS,
                "top_p": TEST_TOP_P,
                "top_k": TEST_TOP_K,
                "user": TEST_USER,
                "n": TEST_N,
                "suffix": TEST_SUFFIX,
                "echo": TEST_ECHO,
                "error_behavior": TEST_ERROR_BEHAVIOR,
                "use_raw_prompt": TEST_USE_RAW_PROMPT,
            },
            "timeout": TEST_TIMEOUT,
        }
        Completion.create(**kwargs)
        mocked_request.assert_called_once_with(**expected_request)

    @patch('databricks_genai_inference.Completion._get_streaming_response')
    def test_completion_request_streaming(self, mocked_request):
        kwargs = {
            "model": COMPLETION_MODEL_NAME,
            "prompt": [COMPLETION_PROMPT_1, COMPLETION_PROMPT_2],
            "temperature": TEST_TEMPERATURE,
            "stop": TEST_STOP,
            "max_tokens": TEST_MAX_TOKENS,
            "top_p": TEST_TOP_P,
            "top_k": TEST_TOP_K,
            "user": TEST_USER,
            "timeout": TEST_TIMEOUT,
            "n": TEST_N,
            "suffix": TEST_SUFFIX,
            "echo": TEST_ECHO,
            "error_behavior": TEST_ERROR_BEHAVIOR,
            "use_raw_prompt": TEST_USE_RAW_PROMPT,
            "stream": True
        }
        expected_request = {
            "url": f'{TEST_HOST_NAME}/serving-endpoints/databricks-{COMPLETION_MODEL_NAME}/invocations',
            "headers": {
                'authorization': "Bearer " + TEST_API_KEY,
                'Content-Type': 'application/json'
            },
            "json": {
                "model": COMPLETION_MODEL_NAME,
                "prompt": [COMPLETION_PROMPT_1, COMPLETION_PROMPT_2],
                "temperature": TEST_TEMPERATURE,
                "stop": TEST_STOP,
                "max_tokens": TEST_MAX_TOKENS,
                "top_p": TEST_TOP_P,
                "top_k": TEST_TOP_K,
                "user": TEST_USER,
                "n": TEST_N,
                "suffix": TEST_SUFFIX,
                "echo": TEST_ECHO,
                "error_behavior": TEST_ERROR_BEHAVIOR,
                "use_raw_prompt": TEST_USE_RAW_PROMPT,
                "stream": True
            },
            "timeout": TEST_TIMEOUT,
        }
        Completion.create(**kwargs)
        mocked_request.assert_called_once_with(**expected_request)

    @patch('databricks_genai_inference.Embedding._get_non_streaming_response')
    def test_embedding_request_non_streaming(self, mocked_request):
        kwargs = {
            "model": EMBEDDING_MODEL_NAME,
            "instruction": EMBEDDING_INSTRUCTION,
            "input": [EMBEDDING_INPUT_1, EMBEDDING_INPUT_2],
            "user": TEST_USER,
            "timeout": TEST_TIMEOUT,
        }
        expected_request = {
            "url": f'{TEST_HOST_NAME}/serving-endpoints/databricks-{EMBEDDING_MODEL_NAME}/invocations',
            "headers": {
                "authorization": "Bearer " + TEST_API_KEY,
                "Content-Type": "application/json"
            },
            "json": {
                "model": EMBEDDING_MODEL_NAME,
                "instruction": EMBEDDING_INSTRUCTION,
                "input": [EMBEDDING_INPUT_1, EMBEDDING_INPUT_2],
                "user": TEST_USER,
            },
            "timeout": TEST_TIMEOUT,
        }
        Embedding.create(**kwargs)
        mocked_request.assert_called_once_with(**expected_request)
