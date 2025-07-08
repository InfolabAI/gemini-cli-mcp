# Gemini MCP Server

Claude Code에서 Gemini AI를 MCP 서버로 사용할 수 있게 해주는 도구입니다.

## 주요 이점

1. **대용량 파일 분석**: Gemini의 거대한 컨텍스트 윈도우를 활용하여 대용량 파일과 디렉토리를 한 번에 분석 가능
2. **토큰 절약**: Claude Code의 토큰 사용량을 절약하면서도 강력한 AI 분석 기능 활용

이 서버는 로컬에 설치된 `gemini` CLI 도구를 사용하여 작동합니다.

## 사전 요구사항

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) 패키지 매니저
- [gemini](https://github.com/replit/gemini) CLI 도구

## 설치

1. 저장소 클론:
```bash
git clone <repository-url>
cd mcp-gemini
```

2. 의존성 설치:
```bash
uv sync
```

3. Gemini CLI 설치:
```bash
# macOS
brew install replit/gemini/gemini

# 또는 직접 설치
curl -fsSL https://gemini.replit.com/install.sh | sh
```

## Tools

- **run_gemini**
  - Gemini를 이용해서 파일, 디렉토리, URL의 대량 정보를 요약합니다
  - 입력:
    - `prompt` (string): Gemini에 전달할 프롬프트
    - `file_dir_url_path` (string): 분석할 파일, 디렉토리 또는 URL 경로

## 사용 예시

```
"이 Python 파일의 주요 기능을 한국어로 요약해주세요"
"프로젝트 구조를 분석하고 개선점을 제안해주세요"
"이 웹페이지의 핵심 정보를 추출해주세요"
```

## Configuration 

Claude Code에서 사용하려면 MCP 서버 설정을 추가하세요:

`~/.claude.json` 파일에 다음 설정을 추가:

```json
{
  "mcpServers": {
    "gemini-mcp-server": {
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

**참고**: `/path/to/your/project/`를 실제 프로젝트 경로로 변경하세요.

## 개발

서버 직접 실행(실행 후, 멈춰있는 것이 정상임):
```bash
uv run python gemini_mcp_server.py
```

테스트:
```bash
uv run python test_gemini_mcp.py
```

### Debugging

MCP 서버는 stdio를 통해 통신하므로 디버깅이 어려울 수 있습니다. [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 사용을 권장합니다.

## uv 설치

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


## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.