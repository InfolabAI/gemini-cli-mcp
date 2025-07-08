# Gemini MCP Server

Claude Code에서 Gemini AI를 MCP 서버로 사용할 수 있게 해주는 도구입니다.

## 주요 이점

1. **대용량 파일 분석**: Gemini의 거대한 컨텍스트 윈도우를 활용하여 대용량 파일과 디렉토리를 한 번에 분석 가능
2. **토큰 절약**: 무료로 제공되는 Gemini CLI를 이용해서 Claude Code의 토큰 사용량을 절약하면서도 Claude Code만의 강력한 기능을 활용 가능

이 서버는 로컬에 설치된 `gemini` CLI 도구를 사용하여 작동합니다.

## 사전 요구사항

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) 패키지 매니저
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) CLI 도구

## 설치

- 저장소 클론:
```bash
git clone <repository-url>
cd mcp-gemini
```

- uv 설치

uv는 시스템 레벨에 설치해야 합니다 (Python 가상환경과 독립적으로 작동):

```bash
# Linux/macOS (권장)
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS Homebrew
brew install uv

# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 설치 확인
uv --version
```

- 의존성 설치:
```bash
uv sync
```

## Tools

- **run_gemini**
  - Gemini를 이용해서 파일, 디렉토리, URL의 대량 정보를 처리합니다
  - 입력:
    - `prompt` (string): Gemini에 전달할 프롬프트
    - `file_dir_url_path` (string): 분석할 파일, 디렉토리 또는 URL 경로

## Configuration 

Claude Code에서 사용하려면 MCP 서버 설정을 추가하세요:

Linux 의 경우, `~/.claude.json` 파일에 다음 설정을 추가:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "/path/to/your/project/gemini_mcp_server.py"
      ],
      "env": {}
    }
  }
}
```

**참고**: `/path/to/your/project/`를 다운받은 git 프로젝트 경로로 변경하세요.

## 개발

- 서버 직접 실행(실행 후, 멈춰있는 것이 정상임)
```bash
uv run python gemini_mcp_server.py
```

- 테스트
```bash
uv run python test_gemini_mcp.py
```

- Debugging

MCP 서버는 stdio를 통해 통신하므로 디버깅이 어려울 수 있습니다. [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 사용을 권장합니다.

- 주의할 점

subprocess.run 을 사용할 때 `shell=True` 옵션을 사용해야 합니다. 이는 MCP 서버 환경에서 쉘을 통해 명령을 실행하기 위함입니다. 이 옵션이 없으면, Gemini CLI 명령 실행 시, 대기 상태에 빠질 수 있습니다. 그 이유는, MCP 서버는 stdio 모드로 실행되어 stdin/stdout이 파이프로 연결되는데, 일부 CLI 도구(특히 Node.js 기반)는 tty 환경에서와 파이프 환경에서 다르게 동작하기 때문입니다. 터미널에서 직접 `run_gemini.py` 를 실행될 때는 완전한 tty 환경 제공하기 때문에 `shell=True` 옵션이 필요하지 않습니다.


## 사용 예시

Claude Code에서 MCP 서버를 사용하여 Gemini CLI를 호출할 수 있습니다. 예를 들어, 다음과 같이 사용할 수 있습니다:
- Claude Code에서의 Gemini 호출과 Gemini 의 응답의 예

```
╭───────────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                         │
╰───────────────────────────────────────────────────╯


> gemini 로 gemini_mcp_server.py 요약 분석 진행해

● I'll analyze the gemini_mcp_server.py file using the Gemini MCP server to provide a summary.

● gemini-mcp-server:run_gemini (MCP)(prompt: "이 Python 파일의 주요 기능과 구조를 한국어로 요약해주세요. 클래스, 함수, 주요 로직을 포함해서 분석해주세요.", file_dir_url_path:
                                    "gemini_mcp_server.py")
  ⎿ { 
    "result": "[dotenv@16.6.0] injecting env (2) from ../../../.env\n[dotenv@16.6.0] injecting env (2) from ../../../.env\n[dotenv@16.6.0] injecting env (2) from ../../../.env\nMCP STDERR (github): GitHub MCP Server running on stdio\n\nMCP STDERR (sequential-thinking): Sequential Thinking MCP Server running on stdio\n\nMCP STDERR (context7): Context7 Documentation MCP Server running on stdio\n\n이 Python 파일(`gemini_mcp_server.py`)은 Gemini CLI 도구를 MCP(Multi-Agent Communication Protocol) 서버를 통해 외부에서 호출할 수 있도록 래핑하는 역할을 합니다.\n\n**주요 기능 및 구조:**\n\n*   **FastMCP 서버 초기화**: `FastMCP(\"Gemini MCP Server\")`를 사용하여 `mcp`라는 MCP 서버 인스턴스를 생성합니다. 이는 이 파일이 MCP 프로토콜을 통해 다른 에이전트와 통신할 수 있는 서버임을 나타냅니다.\n*   **`run_gemini` 함수 (도구)**:\n    *   `@mcp.tool()` 데코레이터가 붙어 있어, 이 함수가 MCP 서버를 통해 외부에서 호출될 수 있는 \"도구\"로 노출됨을 의미합니다.\n    *   **인자**: `prompt` (Gemini에 전달할 프롬프트)와 `file_dir_url_path` (분석할 파일, 디렉토리 또는 URL 경로)를 받습니다.\n    *   **주요 로직**:\n 1.  `file_dir_url_path`를 `prompt`에 추가하여 Gemini CLI에 전달될 최종 프롬프트를 구성합니다.\n        2.  `subprocess.run`을 사용하여 실제 `gemini` CLI 명령을 실행합니다. 이 때 `shell=True` 옵션을 사용하여 쉘을 통해 명령을 실행하며, 이는 MCP 서버 환경에서 필요하다고 주석에 명시되어 있습니다.\n        3.  `gemini -m gemini-2.5-flash -p \"...\"` 형식으로 명령어를 구성합니다.\n        4.  명령 실행 중 발생할 수 있는 `subprocess.TimeoutExpired` (60초 시간 초과), `FileNotFoundError` (Gemini CLI가 설치되지 않은 경우), 그리고 일반 `Exception`을 처리하여 사용자에게 적절한 에러 메시지를 반환합니다.\n        5.  Gemini CLI 실행이 성공하면 표준 출력(`stdout`)을 결과로 반환하고, 에러가 발생하면 에러 메시지를 반환합니다.\n*   **서버 실행**: `if __name__ == \"__main__\":` 블록 내에서 `mcp.run()`을 호출하여 MCP 서버를 시작합니다. 이는 이 스크립트가 직접 실행될 때 서버가 구동됨을 의미합니다.\n\n**요약:**\n\n`gemini_mcp_server.py`는 `FastMCP` 프레임워크를 사용하여 Gemini CLI를 외부에서 호출 가능한 도구(`run_gemini` 함수)로 제공하는 간단한 서버입니다. 이 서버는 특정 프롬프트와 파일/디렉토리/URL 경로를 인자로 받아 Gemini CLI를 실행하고 그 결과를 반환하며, 실행 중 발생할 수 있는 다양한 오류를 처리합니다."
    }
```

- Gemini의 응답을 이용한 Claude Code 의 최종 출력

```
● gemini_mcp_server.py는 Gemini CLI를 MCP 서버로 래핑한 파일입니다. FastMCP 프레임워크를 사용하여 run_gemini 도구를 제공하며, 프롬프트와 파일 경로를 받아 Gemini CLI를 실행하고 결과를 반환합니다. 60초 타임아웃과 에러 처리가 포함되어 있습니다.
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
