#!/usr/bin/env python3
"""
Gemini MCP Server
"""

import os
import subprocess
from mcp.server.fastmcp import FastMCP

# MCP 서버 초기화
mcp = FastMCP("Gemini MCP Server")


@mcp.tool()
def run_gemini(prompt: str, file_dir_url_path: str) -> dict:
    """
    Gemini를 사용하여 프롬프트를 실행합니다.

    Args:
        prompt: Gemini에 전달할 프롬프트
        file_dir_url_path: 분석할 파일, 디렉토리 또는 URL 경로

    Returns:
        dict: 실행 결과 또는 에러 메시지
    """

    prompt = prompt + f" (분석할 파일, 디렉토리 또는 URL 경로: {file_dir_url_path})"
    try:
        # Gemini 명령 실행
        cmd = [
            "gemini",
            "-m", "gemini-2.5-flash",
            "-p", prompt
        ]

        # shell=True로 실행 (MCP 서버 환경에서 필수)
        shell_cmd = ' '.join(
            [f'"{arg}"' if ' ' in arg else arg for arg in cmd])

        result = subprocess.run(
            shell_cmd,
            shell=True,  # 필수
            capture_output=True,
            text=True,
            timeout=360,
            stdin=subprocess.DEVNULL
        )

        # 에러 체크
        if result.returncode != 0:
            return {"error": f"Gemini 실행 오류: {result.stderr}"}

        # 결과 반환
        return {"result": result.stdout.strip()}

    except subprocess.TimeoutExpired:
        return {"error": "Gemini 실행 시간 초과 (60초)"}
    except FileNotFoundError:
        return {"error": "Gemini CLI가 설치되어 있지 않습니다. 'gemini' 명령을 사용할 수 있는지 확인하세요."}
    except Exception as e:
        return {"error": f"실행 중 오류 발생: {str(e)}"}


if __name__ == "__main__":
    # MCP 서버 실행
    mcp.run()
