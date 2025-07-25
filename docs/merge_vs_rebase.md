## Merge vs Rebase

### Merge
- 두 브랜치를 하나로 합치는 명령어.
- 기존 커밋 기록을 유지하면서 새로운 병합 커밋(Merge Commit)을 생성.
- 브랜치의 작업 이력이 분기된 그대로 보존됨.

```bash
git checkout main
git merge add-image
```

### Rebase
- 브랜치의 기반(base)을 다른 브랜치의 최신 커밋으로 변경.
- 마치 feature 브랜치를 main 브랜치에서 처음부터 분기한 것처럼 기록을 재작성.
- 커밋 히스토리가 깔끔해지지만, 기존 커밋 해시가 변경됨.


## Merge를 추천하는 이유

### 안정성
- 이미 공유된 브랜치(release, main, develop 등)에서 rebase는 커밋 해시 변경으로 협업자에게 문제를 유발한다.
- merge는 기존 커밋을 변경하지 않아 협업 시 충돌과 오류를 최소화할 수 있다.

### 히스토리 보존
- 언제, 어디서 브랜치가 분기되고 병합되었는지 명확히 파악 가능하다.
- 대규모 팀 협업에서 브랜치 흐름을 추적하기 용이하다.

### 실수 방지
- rebase는 push 후 강제 푸시(force push)가 필요할 수 있어, 실수로 다른 사람의 커밋을 덮어쓸 위험이 존재한다.
- merge는 추가 병합 커밋만 생성하므로 안전하다.


### 결론
- 개인 작업 브랜치: rebase로 깔끔하게 관리 가능.

- 공유(협업) 브랜치(main, develop 등): merge를 사용해 안정적으로 통합.