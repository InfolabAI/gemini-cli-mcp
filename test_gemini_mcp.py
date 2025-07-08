#!/usr/bin/env python3
"""
Gemini MCP Server 테스트 스크립트
직접 MCP 서버와 통신하여 테스트합니다.
uv run python gemini_mcp_server.py 명령으로 서버를 실행한 후 사용하세요.
"""

import json
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_gemini_mcp():
    """MCP 서버 테스트"""

    # 서버 실행 명령 (mcpserver list와 동일하게)
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python",
              "gemini_mcp_server.py"],
        env={}
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 서버 초기화
            await session.initialize()

            # 사용 가능한 도구 확인
            tools = await session.list_tools()
            print("사용 가능한 도구:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # run_gemini 도구 테스트
            print("\n테스트 실행:")

            # 테스트 1: 간단한 질문
            result = await session.call_tool(
                "run_gemini",
                arguments={
                    "prompt": "안녕하세요. 간단히 인사해주세요.",
                    "file_dir_url_path": "없음"
                }
            )
            print(f"\n테스트 1 결과:")
            for content in result.content:
                if hasattr(content, 'text'):
                    print(f"  텍스트: {content.text}")
                else:
                    print(f"  내용: {content}")

            # 테스트 2: 파일 분석 (현재 디렉토리의 pyproject.toml)
            result = await session.call_tool(
                "run_gemini",
                arguments={
                    "prompt": "이 파일의 내용을 간단히 설명해주세요.",
                    "file_dir_url_path": "./pyproject.toml"
                }
            )
            print(f"\n테스트 2 결과:")
            for content in result.content:
                if hasattr(content, 'text'):
                    print(f"  텍스트: {content.text}")
                else:
                    print(f"  내용: {content}")


async def main():
    try:
        await test_gemini_mcp()
    except Exception as e:
        print(f"에러 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Gemini MCP 서버 테스트 시작...")
    asyncio.run(main())
