# Assessment 01 提交与版本控制

2026-11-07 核验。继续使用个人仓库的 `main` 分支，保留已经推送的历史。

## 提交到哪里

VS Code、终端和 Codex 都应打开同一个仓库根目录：

```text
C:\Users\Mr. Guo\Documents\GitHub\aim-2627-cpp-cw-20906982
```

远程为 <https://github.com/Orion333333/aim-2627-cpp-cw-20906982>，本地 `main` 跟踪 `origin/main`。课程允许直接在 `main` 开发。当前聊天最初从 `D:\cpp` 启动，今后从上述仓库目录开启作业聊天，便于会话与项目对应。

| 内容 | 位置与处理方式 |
| --- | --- |
| 解答 | `src/main/A1_q*.cpp`、`A1_b*.cpp`，仅改实现区 |
| 设计、复杂度与 AI 声明 | `README.md` 的个人说明区 |
| 本地测试、工作记录和本指南 | `local_tests/` |
| 自动生成的会话归档 | `.agent-sessions/bundles/`，随真实提交保存 |
| 会话文本导出、虚拟环境、评分报告和编译产物 | 使用现有忽略目录，不手动强制加入 Git |

固定测试、类型、题面、工具、工作流和根目录配置维持模板原样。此次新增文件均放在允许的 `local_tests/` 中。

## 什么时候提交

继续采用每题三个有实际产出的阶段。阶段可以合并，依据改动内容决定。

| 阶段 | 一次提交包含的内容 | 中文 Summary 示例 |
| --- | --- | --- |
| MVP | 本题实现、基础测试、README 和工作记录 | 实现Q6目标选择MVP，补充基础测试和说明 |
| 最小能力边界 | 新增边界测试、范围说明和实际结果；有修复则包含修复 | 明确Q6最小能力边界，补充规模测试 |
| 完成本地验收 | 独立对照测试、必要修复及最终验证记录 | 补充Q6随机对照测试，更新验收结果 |

一次提交应能说明一个具体变化。仅回答问题或重复运行已有测试，通常不需要额外提交；新增有用证据时，可以提交记录，并在 Summary 中写清“记录”或“更新验证结果”。实际只改文档时，避免写成“实现功能”。

目前共 16 个提交，扣除初始提交为 15 个增量，已达到模板的提交粒度参考线。该参考线不决定成绩，无须为了数量拆分修改。

早期 `Q1 draft`、`确认了一下边界` 较笼统；`2913986` 实际只更新工作记录；`221057b` 的标题末尾多了反引号。保留这些真实历史，从下一次提交起使用“题号＋实际动作”的标题。复制 Summary 代码块内的文字即可。

## 每个阶段的操作顺序

1. 保存 VS Code 文件，检查 `git status -sb` 和差异，确认正在上述个人仓库工作。
2. 运行本题需要的验证，将输入范围、结果和未完成项写入工作记录。
3. 在 VS Code“源代码管理”逐项暂存，或在 GitHub Desktop 勾选本阶段文件。查看暂存差异，确认实现、测试与说明对应。
4. 填入中文 Summary，正常提交一次，等提交钩子全部结束。
5. 检查最终提交及会话归档，再 Push。每个通过本地验收的阶段推送一次即可。

下列命令用于查看暂存内容和提交结果：

```powershell
git diff --cached --stat
git diff --cached
git log -1 --oneline
git show --stat HEAD -- .agent-sessions/bundles/
git status -sb
```

会话工具会在正常提交后把归档 amend 到刚产生的提交，因此最终 SHA 以钩子完成后的 `git rev-parse HEAD` 为准。不要在钩子运行中推送，也不要手动运行 post-commit。归档出错时先查看错误和 `git status`，避免连续点击提交。

本轮没有暂存、提交或推送。下一次提交应包含本指南、导出脚本及测试、README、工作记录；归档由工具生成。首次真实提交后，需要确认最终提交中确有对应 bundle。本轮只实测了提交前链路，尚未验证提交后打包。

## 会话归档的配置和覆盖范围

当前克隆已安装 `agent-session-commit[pre-commit]==0.1.5`，专用环境为 `.venv-agent-session-commit/`，官方框架的 pre-commit 和 post-commit hooks 已安装。模板 `.pre-commit-config.yaml` 保持原样。

本聊天的原始工作目录是 `D:\cpp`，原生 Codex 收集器按仓库目录筛选时会漏掉它。因此使用 Custom 来源：`local_tests/export_agent_sessions.py` 按本作业聊天 ID 或准确的仓库工作目录选择真实会话，导出用户和助手可见文字到 `.agent-sessions/source/codex-visible/`。提交前通过本地 legacy hook 刷新来源，随后由官方框架处理归档。

导出保留原时间、原始行号、原工作目录和校验哈希；原始会话文件留在本机。系统与开发者上下文、内部推理、工具载荷、工作区上下文和非文字附件不在导出范围内。这是有明确范围的文字记录，README 和清单如实说明缺口，不能宣称原始会话已完整归档。会话正在进行时，尚未写入本地文件的内容需在后续导出时补入。

Q1–Q5 开发时尚未安装归档工具。现有真实记录将在下一次正常提交中补充导入，不修改过去的提交，也不声称旧提交当时已含归档。教师对覆盖范围的最终判断仍待确认。

检查来源与刷新导出：

```powershell
.\.venv-agent-session-commit\Scripts\python.exe -B local_tests/export_agent_sessions.py
.\.venv-agent-session-commit\Scripts\agent-session-commit.exe status
```

`status` 能识别来源不等于归档完成。应在真实提交之后结合 `git show` 核对 bundle，推送后再确认 GitHub 上的最终提交。

新 clone 需要单独安装。以下命令在仓库根目录执行，要求已有 Python 3.10+：

```powershell
python -m venv .venv-agent-session-commit
.\.venv-agent-session-commit\Scripts\python.exe -m pip install 'agent-session-commit[pre-commit]==0.1.5'
.\.venv-agent-session-commit\Scripts\python.exe -B local_tests/export_agent_sessions.py
.\.venv-agent-session-commit\Scripts\agent-session-commit.exe install --pre-commit --agent custom --source '.agent-sessions/source/codex-visible'
.\.venv-agent-session-commit\Scripts\python.exe -B local_tests/export_agent_sessions.py --install-hook
```

这些步骤需要本机存在属于本仓库的真实 Codex 会话。重新克隆或迁移电脑后，先核对实际来源；移动虚拟环境后重新安装 hooks。脚本不会覆盖不属于它的 legacy hook。

## 同步与网络

此次联网核对时，本地 HEAD 和远端 `main` 都是 `f7b26261528d22bdc1375d885ef888460a0a7060`。此后的同步状态每次重新检查。

换电脑工作前先保存、提交或妥善保留当前改动。在干净工作区获取远端状态：

```powershell
git fetch origin
git status -sb
```

若仅落后，使用 `git pull --ff-only`。出现分叉时先查双方历史，再决定如何合并。已推送的作业历史保留原样，常规流程不使用 squash、rebase 或 force push。

终端直连 GitHub 曾失败。当前仅在本仓库 `.git/config` 为 GitHub 配置了系统正在使用的代理 `http://127.0.0.1:7897`，配置后 `git ls-remote origin refs/heads/main` 成功。该端口依赖本机代理程序。若今后改用直连，可移除这条本地配置：

```powershell
git config --local --unset 'http.https://github.com/.proxy'
```

当前索引为 LF、Windows 工作文件为 CRLF，符合现有 `core.autocrlf=true` 的行为。保持现状，避免整仓格式变化。

## 推送与正式交卷

Commit 保存本地版本，Push 同步到 GitHub。最终交卷还需按 README 提交回执，填写最终 `main` 提交号并保留对应 Actions 链接。

本轮完整本地检查中，Q1–Q5 的可见组各通过 2/2；Q6–Q8 尚未实现，`--require-core` 检查退出码为 1。公开自动分为 31.2/60，选做分为 0/20，不能视为正式总成绩。远程 Actions 状态未核验。

完成 Q1–Q8 后再做整体验收。确认最终 `main` 的 CI 全部通过，核对 AI 声明及归档、最终 SHA 与回执要求，再完成正式提交。
