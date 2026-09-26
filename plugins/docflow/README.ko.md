# docflow

Claude Code 프로젝트용 문서 구조·작업 흐름 규칙입니다. 모든 프로젝트가 같은 모양을 갖게 해서, Claude와 사람 모두 "이 문서는 어디에 두나", "어느 문서가 최신인가"를 헷갈리지 않게 합니다.

[English](README.md)

## 규칙

```
<프로젝트>/
├── CLAUDE.md        ← 프로젝트 설정 · 현재 작업 · Backlog · Gotchas
├── README.md        ← 외부 독자용, 그 자체로 완결된 소개
└── docs/
    ├── product.md   ← 제품 정의의 단일 소스
    ├── plan/        ← master-plan.md (+ Phase가 시작될 때만 phase 파일)
    ├── architecture/
    ├── design/
    ├── review/      ← <type>-<topic>-<YYYYMMDD>.md
    └── reference/
```

- **루트 문서는 두 개뿐**: `CLAUDE.md`와 `README.md`만 둡니다. 언어별 README(README.ko.md 등)와 LICENSE, CHANGELOG, CONTRIBUTING 같은 표준 파일은 예외로 허용합니다.
- **`docs/`는 하위 폴더 5개로 고정**: 새 폴더는 만들지 않습니다. 어디에도 맞지 않는 문서는 `reference/`에 둡니다.
- **`product.md`가 허브**: 내부 문서는 제품 정의를 반복하지 않고 `product.md`를 링크합니다. README는 외부 독자용이라 예외로, 그 자체로 완결되게 씁니다.
- **CLAUDE.md가 작업 파일을 대신**: 지금 하는 일은 *현재 작업*, 나중에 할 일은 *Backlog*(한 줄씩), 또 밟을 함정은 *Gotchas*(지우지 않음)에 적습니다. `tasks/`나 `TODO.md`는 쓰지 않습니다.
- **문서는 항상 최신으로**: 구조·설계·디자인을 바꾼 작업은 같은 작업 안에서 해당 문서도 고칩니다. 새 문서를 만들지 말고 기존 문서를 수정하며, 현재 상태만 적습니다.
- **레포냐, 문서 도구냐**: 판단이나 에이전트의 입력이 되는 문서는 git에 둡니다. 최신 상태만 보면 되는 것(대시보드, 프로젝트 현황, 범용 가이드)은 Notion 같은 문서 도구에 둡니다.

## 설치

```
claude plugin marketplace add solpop-arch/claude-plugins
claude plugin install docflow@solpop
```

## 스킬

| 스킬 | 실행 방식 | 하는 일 |
|---|---|---|
| `/docflow:init` | 직접 실행 | `docs/` 뼈대, `product.md`와 `master-plan.md` 템플릿, 4섹션 `CLAUDE.md`(규칙 요약 포함)를 만듭니다. 기존 파일은 덮어쓰지 않습니다. CLAUDE.md가 이미 있으면 무엇을 덧붙일지 먼저 보여주고 동의를 받은 뒤 추가합니다. |
| `/docflow:audit` | 직접 실행 | 구조를 점검한 뒤(루트에 흩어진 문서, 규칙에 없는 `docs/` 폴더, 작업 파일, 빠진 섹션, review 파일명), 내용 수준 규칙도 검토합니다. 보고만 하고, 동의 없이 아무것도 바꾸지 않습니다. |
| `rules` | Claude가 자동으로 불러옴 | 전체 규칙집입니다. Claude가 문서를 만들거나 옮길 때, CLAUDE.md를 고칠 때 불러옵니다. |

**팁**: 문서가 이미 있는 프로젝트라도 `/docflow:init`을 한 번 실행하세요. init이 `CLAUDE.md`에 넣는 규칙 요약이 있어야 모든 세션에서 규칙이 적용됩니다. 자동으로 불러오는 스킬은 Claude가 관련 있다고 판단할 때만 불러와지기 때문입니다.

## 라이선스

MIT
