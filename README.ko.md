# solpop — Claude Code 플러그인

작은 Claude Code 플러그인 마켓플레이스입니다.

[English](README.md)

## 플러그인

| 플러그인 | 하는 일 |
|---|---|
| [docflow](plugins/docflow/README.ko.md) | 프로젝트 문서 구조 규칙입니다. 루트에는 `CLAUDE.md`와 `README.md`만 두고, 나머지는 `product.md`를 중심으로 한 고정된 `docs/` 구조에 둡니다. 작업 관리는 별도 작업 파일 대신 `CLAUDE.md`의 4개 섹션으로 합니다. `/docflow:init`으로 구조를 만들고 `/docflow:audit`으로 점검합니다. |

## 설치

```
claude plugin marketplace add solpop-arch/claude-plugins
claude plugin install docflow@solpop
```

세션 안에서는 `/plugin install docflow --marketplace solpop-arch/claude-plugins` 한 줄로도 설치할 수 있습니다.

## 라이선스

MIT
