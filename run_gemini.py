#!/usr/bin/env python3
"""
Gemini 실행 스크립트
"""

import sys
import os
import subprocess
import json


def run_gemini(prompt):
    """Gemini를 실행하고 결과를 반환"""
    try:
        # Gemini 명령 실행
        cmd = [
            "gemini",
            "-m", "gemini-2.5-flash",
            "-p", prompt
        ]
        
        # 명령 실행
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            env={**os.environ, "PATH": os.environ.get("PATH", "")}
        )
        
        # 에러 체크
        if result.returncode != 0:
            return {"error": f"Gemini 실행 오류: {result.stderr}"}
        
        # 결과 반환
        return {"result": result.stdout}
        
    except subprocess.TimeoutExpired:
        return {"error": "Gemini 실행 시간 초과"}
    except Exception as e:
        return {"error": f"실행 중 오류 발생: {str(e)}"}


def main():
    """메인 함수"""
    if len(sys.argv) != 2:
        print(json.dumps({"error": "프롬프트가 필요합니다"}, ensure_ascii=False))
        sys.exit(1)
    
    prompt = sys.argv[1]
    result = run_gemini(prompt)
    
    # JSON 형태로 결과 출력
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()