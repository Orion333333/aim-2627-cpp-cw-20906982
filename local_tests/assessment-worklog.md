# Assessment 01 作业协作与 Git 记录

创建日期：2026-11-07（北京时间）  
最后更新：2026-11-07（北京时间）

## 1. 用途与当前方向

这份文档持续记录本次作业的方向、决定、实现进度、验证证据和实际产出，方便在 VS Code 中协作与后续接续。

- 目标：完成 AIM 2627 C++ Assessment 01，并能够理解和解释自己的实现。
- 已确认：在用户已经克隆、并在 VS Code 打开的个人仓库中工作。
- 已确认：由用户指引下一步任务、推进顺序和具体协作方式；助手不把自己的建议记成用户决定。
- 已确认：用户要求把方向和产出记录在工作空间中的 Git 文档里。
- 已确认的当前方向：用户要求完成 B1；保留已验证解答，补齐独立随机参考与连续输出保留检查，重新实跑 B1 并更新合并验收结果，同步 README。
- Q1 技术路线：保留 MVP 的条件分支、整数运算和字符串拼接；逐条核对正式规范后，未发现需要改变算法的问题。
- 待定：后续逐段讲解、用户修改及其他题目的推进安排。
- 已确认：开始 B1 选做挑战；B2 是否选做待定。

## 2. 仓库与要求入口

| 项目 | 当前已核实的信息 |
| --- | --- |
| 个人远程仓库 | <https://github.com/Orion333333/aim-2627-cpp-cw-20906982> |
| 本地目录 | `C:\Users\Mr. Guo\Documents\GitHub\aim-2627-cpp-cw-20906982` |
| 当前分支 | `main`（2026-11-07 本地检查） |
| 建档前 HEAD | `a80983b91bf8195fad769163f0828b29ab7f4b61`，`Initial commit` |
| 建档前工作区 | 干净，无本地未提交改动 |
| Q2 开始前 HEAD | `02f7ef75deba1f1bdf2b618075161f13c748e76d`，工作区干净；Q1 代码已在 `7b96887` 提交中 |
| Q2 完成验证开始前 HEAD | `8d92775ae35703e8279bf5bee7ade23ff4f56bc4`，工作区干净；该提交已包含 Q2 MVP |
| Q3 开始前 HEAD | `221057b16eba56754d5fa55bf6c52db349d888a2`，工作区干净；本轮改动尚未提交 |
| Q3 边界任务开始前 HEAD | `b79a8973b02720b0ef8dfd020127419b40c45a29`，工作区干净；Q3 MVP 已包含在该提交中 |
| Q3 完成任务开始前 HEAD | `c3b838d0a0ff3fa6cc09fa15b21c1fe998541ec4`，工作区干净；main 较本地 origin/main 领先 1 个提交 |
| Q4 开始前 HEAD | `5cef47061a4a7be1fcd2721d43f8adba70584966`，工作区干净；本地 main 与保存的 origin/main 一致 |
| Q4 边界任务开始前 HEAD | `32ecdad860089327b28d8d79e77d72fe2fef77cf`，工作区干净；Q4 MVP 已包含在该提交中 |
| Q4 完成任务开始前 HEAD | `c66f6964123a1f83e9ce11f2627fb82e7856fc4d`，工作区干净；开始时 main 比本地 origin/main 领先 1 个提交 |
| Q5 开始前 HEAD | `4c6dbea2e8bb684c8502140f1558b0309be46017`，工作区干净；本地 main 与保存的 origin/main 一致 |
| Q5 边界任务开始前 HEAD | `4d879e455664557484cb5662991ad23365808540`，工作区干净；Q5 MVP 已包含在该提交中 |
| Q5 完成任务开始前 HEAD | `c3b0f3bd7008abaecd64655b59abb84c9dfb5dd7`，工作区干净；本地 main 与保存的 origin/main 一致 |
| 版本控制优化开始前 HEAD | `f7b26261528d22bdc1375d885ef888460a0a7060`，工作区干净；本轮联网核对远端 main 与此一致 |
| Q6 MVP 开始前 HEAD | `f7b26261528d22bdc1375d885ef888460a0a7060`；main 与本地保存的 origin/main 一致，上一轮版本控制优化的两份已跟踪文档及三个新增文件仍未提交，暂存区为空 |
| Q6 边界任务开始前 HEAD | `d995ef8978e6fe0e8413fa6195f15f7ffae82d15`，工作区干净；Q6 MVP、前轮优化与首个会话 bundle 均已提交；本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q6 完成任务开始前 HEAD | `f1d255342edba5b2a333de92a5898b66afadadf0`，工作区干净；Q6 规模测试已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q7 MVP 开始前 HEAD | `f2e4c3032e2382ace347dca63500c74cdc582cfc`，工作区干净；Q6 随机验证和完成记录已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q7 边界任务开始前 HEAD | `3effe9eb90c3677b16ca8037c2a7608c3f0e95f5`，工作区干净；Q7 MVP 已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q7 完成任务开始前 HEAD | `2e77b39a9aa25f87335e9b1fa791770dfc0bdd9f`，工作区干净；Q7 规模测试已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q8 MVP 开始前 HEAD | `12b17d33d8b40ae5f0d4635cb2f983ad767f7092`，工作区干净；Q7 随机验证和完成记录已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| Q8 边界任务开始前 HEAD | `35450762013e8ff601068632a7458bb30d2a0d60`，工作区干净；Q8 MVP 已提交，本地 main 比保存的 origin/main 领先 1 个提交，本轮未联网刷新 |
| Q8 完成任务开始前 HEAD | `4954375514a1da150d76ae0b71ab93938cf22581`，开始时工作区干净、本地 main 较保存的 origin/main 领先 1；任务中该跟踪引用更新为同一 HEAD，本轮未主动联网刷新或推送 |
| B1 MVP 开始前 HEAD | `b613c33a4f4f7bae6d09613bdb0cb34a32356c6c`，工作区干净；Q8 完成产出和此前注释删除均已提交，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| B1 边界任务开始前 HEAD | 仍为 `b613c33a4f4f7bae6d09613bdb0cb34a32356c6c`；前轮 B1 解答、MVP 测试和三份文档仍未提交，暂存区为空，本地 main 与保存的 origin/main 一致，本轮未联网刷新 |
| B1 完成任务开始前 HEAD | `0581ff763b3ac214bcc0a1df17d5beefaa6a0fe0`，工作区干净；B1 MVP 和边界已合并提交，本地 main 较保存的 origin/main 领先 1 个提交，本轮未联网刷新 |
| 环境与提交说明 | [README](../README.md) |
| Markdown 题面 | [PROBLEM.md](../PROBLEM.md) |
| 正式规格入口 | [题面.pdf](../题面.pdf)，README 指定以该 PDF 为准 |

以上 Git 状态是检查时的本地快照，不代表之后的远程状态。每次继续工作时重新查看当前文件和 Git 差异。

已阅读线上 README 和 Markdown 题面；2026-11-07 已提取并核对当前仓库正式 PDF 第 5～22 页（页脚页码 4～21）的 Q1–Q8 与 B1 接口、规范和样例，与对应 Markdown 要求一致。B2 的正式 PDF 尚未逐题核对。

Q4 MVP 阶段临时下载 PDF 读取库曾两次遇到 SSL 网络错误。Q4 边界任务中改用 PowerShell 下载，校验文件哈希后成功提取正式 PDF 第 11、12 页，已完成六条规范、流解析提示与样例的直接复核；临时读取库已清理。

## 3. 协作与记录规则

1. 先说明目标、当前输入和关键假设；存在影响实现的歧义时向用户确认。
2. 用户在 VS Code 保存文件后，助手读取磁盘上的最新版本；不能假定未保存的编辑已同步。
3. 修改前检查已有差异，保留用户已写内容；代码修改限定在题目允许的实现区。
4. 实际完成工作后更新本记录，分别写清计划、已完成、已验证和待确认内容。
5. 测试必须保留实际输入、预期、实际结果和运行方式；未运行就记“未运行”，不填写推测结果。
6. 不把公开自测结果写成正式成绩；本地测试、GitHub CI 和教师验收分别记录。
7. Git 提交或推送按用户后续明确指令执行；建档本身不代表已经提交或推送。
8. 每一次给我答复前，先自己自检代码，可以考虑自己找地方模拟运行一下，或是你有什么好方法，可以自己决定用其他方法，提高一下答复质量就好了
9. 每次完成任务后，给出建议输入的 summary ，用中文告诉我
10. 持续留意本作业的工作历史。每次任务核对当前分支、工作区、提交内容和跟踪分支，在重要节点记录提交号与文件归属，供用户之后复盘提交位置和版本控制问题。

建议填写的 Summary 按用户要求使用中文，内容对应本次实际改动。

本记录放在 `local_tests/`，因为仓库的修改范围检查允许该目录下新增文件。README 只在末尾个人说明区增加入口。固定类型、公开测试、题面、工具和工作流保持原样。

### README 写作要求

用户于 2026-11-07 提出以下要求，后续编写个人说明时遵循。

1. 删去重复表达和无必要的反面说明，一个观点说清楚即可。
2. 用具体动作和事实表达，少写空泛措辞与防御性解释。
3. 先说重点，再补必要背景，使用自然的中文语序。
4. 少用破折号和冒号，优先使用完整、直接的句子。
5. 从实际代码和工作记录中提取细节，例如函数名、数值边界、测试结果和修改原因。

## 4. 每题进度

2026-11-07 建档时十题均为模板 `TODO`；目前 Q1–Q8 与 B1 实现及本地验收完成，合并公开检查通过，B2 仍为模板 `TODO`。

| 题号 | 内容 | 实现状态 | 验证结果 | 设计与复杂度记录 |
| --- | --- | --- | --- | --- |
| Q1 | 定点遥测规范化 | 实现与本地验收完成，代码已在 `7b96887` 提交中 | 公开自检 2/2、25 项定向检查、5350 组穷举及检查器 Q1 2/2 均通过 | 见下方 MVP 和完成记录 |
| Q2 | 设备标签维护 | 实现与本地验收完成，MVP 已在 `8d92775` 中，扩展验证已在 `b5866a7` 中 | 公开测试 2/2、25 项定向检查、3 组规模边界及 1000 组随机对照均通过 | 见下方 MVP 和完成记录 |
| Q3 | 窗口异常检测 | 实现与本地验收完成；解答在 `b79a897`、规模测试在 `c3b838d`、随机验证在 `5cef470` | 公开测试 2/2、20 项定向检查、8 组最大规模测试、1000 组随机对照均通过 | 滑动窗口，O(n) 时间、O(1) 工作空间 |
| Q4 | 严格命令事务 | 实现与本地验收完成；解答在 `32ecdad`、规模测试在 `c66f696`、随机验证在 `4c6dbea` | 公开测试 2/2、25 组定向序列、8 组最大行数及 1000 组随机对照均通过 | 字符串流解析、候选值验证后提交，见下方记录 |
| Q5 | 网格邻域风险图 | 实现与本地验收完成；解答在 `4d879e4`、规模测试在 `c3b0f3b`、随机验证在 `f7b2626` | 公开测试 2/2、20 项定向检查、8 组规模和 1000 组随机对照均通过 | 先验证完整地图，再统计四邻域，见下方记录 |
| Q6 | 目标优先级选择 | 实现与本地验收完成；解答在 `d995ef8`、规模测试在 `f1d2553`、随机验证在 `f2e4c3` | 公开自检与检查器各 2/2、30 项定向、8 组规模及 1000 组随机输入的 3000 次调用均通过 | 一次遍历筛选与三级比较，O(n) 时间、O(1) 空间 |
| Q7 | 热量与弹仓仿真 | 实现与本地验收完成；解答在 `3effe9e`、规模测试在 `2e77b39`、随机验证在 `12b17d3` | 公开自检与检查器各 2/2、30 项定向、8 组规模及 1000 组随机输入的 3000 次调用均通过 | 逐帧先冷却再处理请求，O(n) 时间、O(1) 空间 |
| Q8 | 遥测帧综合流水线 | 实现与本地验收完成；解答在 `3545076`、规模测试在 `e21f1b3`、随机验证在 `b613c33` | 公开自检与检查器各 2/2、32 项定向、8 组规模及 1000 组随机输入的 4000 次调用均通过 | 标记表去重并扫描编号，O(n+U) 时间、O(U) 工作空间，U=10000 |
| B1 | 有符号十进制解析（选做） | 实现与本地验收完成；解答、MVP 与边界测试在 `0581ff7`；本轮随机验证未提交 | 公开自检与检查器各 2/2、44 项定向、16 组千字符组合的 64 项检查及 1000 组随机输入的 4000 次调用通过 | 局部累计、乘加前限幅检查、成功后写回，O(n) 时间、O(1) 空间 |
| B2 | 原地稳定压缩（选做） | 是否选做待定，模板 TODO | 未运行 | 待定 |

每题开始后在本节追加记录：当前要求、核心思路、关键边界、修改文件、复杂度、实际验证结果及尚未解决的问题。

### Q1 MVP（2026-11-07）

- 实现文件：[A1_q1.cpp](../src/main/A1_q1.cpp)；只修改原有实现区，保留固定接口、标记和公开 `main`。
- `ratio`：先判断 `max_hp <= 0` 并返回 `-1`；否则将 `hp` 夹到 `[0,max_hp]`，返回 `hp * 100 / max_hp`。
- 整数宽度：题目限制 `hp`、`max_hp` 的绝对值不超过 `10^12`；夹取后的乘积不超过 `10^14`，使用 `long long` 足够，且非负整数除法直接截断。
- `report`：先将电量夹到 `[0,100]`；调用 `ratio` 得到百分比或 `INVALID`，按 60、20 两个端点分档，再拼出严格格式的返回字符串。
- 失败路径：无效最大血量不执行除法；报告仍正常处理电量和状态。没有额外异常、键盘输入、调试输出或共享可变状态。
- 复杂度：按题目限定的数字范围，两函数时间和额外空间均为 `O(1)`，返回字符串长度也有固定上界。
- 编译环境：`D:\mingw64\bin\g++.exe`，GCC 8.1.0；本轮直接编译使用 C++17、`-Wall -Wextra -pedantic`，未产生警告。
- 本地自测文件：[q1_mvp_test.cpp](q1_mvp_test.cpp)，复用实际保存的实现，不修改原公开测试。
- 检查器结果：仅 Q1 的可见组通过 `2/2`，原始权重得分 `8/8`，折合功能分 `4.8/60`。这是仅评测 Q1 的本地结果，不是整份作业成绩。
- 评分报告位于忽略目录 `scores/q1-mvp/`。其中提交号仍为初始 HEAD；本次实现尚未提交，报告同时记录了实际源码哈希。
- 尚未完成：用户逐段理解与核对、完整 PDF 逐页复核、会话归档配置、远程 CI 和教师验收。

本轮实际运行的 PowerShell 命令（在仓库根目录执行）：

```powershell
New-Item -ItemType Directory -Path 'local_tests\build' -Force | Out-Null
g++ -std=c++17 -Wall -Wextra -pedantic src/main/A1_q1.cpp -o local_tests/build/q1_public.exe
.\local_tests\build\q1_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic local_tests/q1_mvp_test.cpp -o local_tests/build/q1_mvp_test.exe
.\local_tests\build\q1_mvp_test.exe
python -X utf8 tools/check.py . --only q1 --output scores/q1-mvp
```

实际输出依次为 `PUBLIC 2/2`、`Q1 boundary tests passed (17 checks)`、`.: auto=4.8/60 bonus=0/20`；编译和运行退出码均为 0。

### Q1 完成与本地验收（2026-11-07）

用户要求沿用 MVP 路线完成 Q1。逐条核对正式 PDF 的六条规范后，已有实现覆盖全部功能要求，因此保留 `ratio`、`report` 的算法，不作无必要的重写。

| 正式规范 | 实现或验证证据 |
| --- | --- |
| 血量范围至正负 `10^12`，电量可以是任意 int | 大血量及 `numeric_limits<int>` 极值的定向测试通过 |
| `max_hp <= 0` 返回 -1，报告使用 INVALID，电量仍处理 | 除法前直接返回；零与负最大血量及完整报告测试通过 |
| 先夹取血量，计算截断的整数百分比 | `long long` 乘积上限 `10^14`；5350 组小范围穷举验证取整不等式 |
| 电量先夹取，再按 20、60 分档 | 19、20、59、60 以及负数、超百和 int 极值的测试通过 |
| 报告格式严格、无空格、补零和尾部换行 | 对完整字符串逐字比较，覆盖编号 0、7、9999 |
| 不修改调用方输入，调用之间独立 | 参数按值传递、无共享可变状态；调用后输入值检查及交替调用测试通过 |

在原本的 [q1_mvp_test.cpp](q1_mvp_test.cpp) 中扩展测试，保留文件名以便复用已有运行命令：

- 定向检查由 17 项扩展到 25 项，增加极端血量、编号端点、输入不变及连续调用检查。
- 对每个 `maximum=1..100`，遍历 `health=-1..maximum+1`，共 5350 组输入。
- 对穷举结果验证 `0 <= percentage <= 100`，以及 `percentage * maximum <= normalized * 100 < (percentage + 1) * maximum`。该验证使用取整的数学定义，不在预期值中重复实现整数除法。
- 最终直接编译增加 `-Werror`，未产生编译警告。

最终实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q1.cpp -o local_tests/build/q1_public.exe
.\local_tests\build\q1_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q1_mvp_test.cpp -o local_tests/build/q1_mvp_test.exe
.\local_tests\build\q1_mvp_test.exe
python -X utf8 tools/check.py . --only q1 --output scores/q1-final
```

实际输出依次为 `PUBLIC 2/2`、`Q1 tests passed (25 directed checks, 5350 exhaustive cases)`、`.: auto=4.8/60 bonus=0/20`，退出码均为 0。最终可见评分报告在忽略目录 `scores/q1-final/`；仅 Q1 可见组通过 `2/2`，不是教师隐藏测试或正式成绩。

本轮没有发现需要修复的功能缺陷，也没有改动 MVP 的解答源码。Q1 功能实现与本地验证已经完成；用户逐段理解、自动会话归档、Git 提交、远程 CI 和正式交卷另行跟进。

### Q2 MVP（2026-11-07）

用户要求实现 Q2 MVP。本轮只修改 [A1_q2.cpp](../src/main/A1_q2.cpp) 的实现区，新增 [q2_mvp_test.cpp](q2_mvp_test.cpp)，更新 README 与本记录。Q1 源码和测试保留原样。

`edit_labels` 按编辑顺序操作 `labels` 副本。`from` 为空时，只有 `to` 非空才追加。其余情况每次从文本开头重新扫描，用 `find` 找逗号、`substr` 取完整标签；首次匹配后替换或删除，并立即结束本次查找。位置 0 是合法匹配位置，找不到逗号使用 `string::npos` 判断。

删除规则分三种情况：后面还有标签时删除当前标签和后面的逗号；匹配末尾标签时删除前面的逗号及该标签；只有一个标签时清空字符串。重复标签保留，比较区分大小写，后续编辑使用更新后的文本位置。

设 n 为原文本长度、m 为编辑次数、L 为处理期间最大文本长度。参数按值复制需要 O(n) 时间；每次编辑最多扫描或移动 O(L) 个字符，总时间为 O(n + m(L + 1))。文本副本、扩容和临时标签合计占 O(L + 1) 空间。

实际验证均通过：

- 原文件公开自检输出 `PUBLIC 2/2`。
- 25 项本地检查输出 `Q2 MVP tests passed (25 checks)`，覆盖空编辑、空名单、追加、空操作、自替换、完整字段、重复、大小写、四种删除位置、变长后的连续编辑、32 字符标签和输入保持不变。
- 仓库检查器只评测 Q2，可见组通过 2/2，原始权重得分 10/10，折合功能分 6/60；这是 Q2 的本地公开自测结果。
- 两次直接编译均使用 C++17 和 `-Wall -Wextra -pedantic -Werror`，未产生警告；编译和运行退出码均为 0。

运行命令（在仓库根目录执行，已有 `local_tests/build/` 目录）：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q2.cpp -o local_tests/build/q2_public.exe
.\local_tests\build\q2_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q2_mvp_test.cpp -o local_tests/build/q2_mvp_test.exe
.\local_tests\build\q2_mvp_test.exe
python -X utf8 tools/check.py . --only q2 --output scores/q2-mvp
```

评分报告保存在忽略目录 `scores/q2-mvp/`。本轮没有发现需要修复的功能缺陷；用户逐段审阅、自动会话归档和正式提交仍待跟进。

### Q2 完成与本地验收（2026-11-07）

用户认可既定路线，要求继续推进并更新 README。本轮保留 Q2 MVP 的解答源码，新增 [q2_validation.py](q2_validation.py)，完成先前计划的规模边界与随机序列验证。

三组规模边界均从恰好 1000 字符的合法名单开始，每组执行 200 次编辑：

1. 追加 200 个长 32 字符的标签，最终文本为 7600 字符，原标签及新增标签顺序与预期一致。
2. 删除全部 31 个标签，后续 169 次空操作，结果为空字符串。
3. 将末尾的 10 字符标签改成 32 字符再改回，循环 100 轮，最终文本与初始文本完全相同。

随机验证使用固定种子 2627，生成 1000 组序列，每组 0～200 次编辑。标签池包含大小写、前缀、后缀、数字、下划线和 32 字符标签。Python 参考方法先拆成标签列表，用列表的首次查找、替换或删除计算预期结果；C++ 仍运行实际保存的字符串实现。两种方法的完整返回字符串逐字比较，1000 组全部一致。

本轮实际运行命令：

```powershell
python -X utf8 local_tests/q2_validation.py
python -X utf8 tools/check.py . --only q2 --output scores/q2-final
```

输出分别为 `Q2 validation passed: 3 scale cases + 1000 random sequences (seed 2627)` 和 `.: auto=6.0/60 bonus=0/20`，退出码均为 0。新验证驱动以 C++17、`-Wall -Wextra -pedantic -Werror` 编译，无警告。对应结果和实际源码哈希保存在忽略目录 `scores/q2-final/`。

README 已写入这些实际结果，并补充三处代码解释：用完整标签范围比较；删除时处理相邻逗号；匹配后 `break`，下一次编辑重新查找位置。本轮未发现功能缺陷，未修改解答算法。用户是否已逐段理解代码尚未确认。

当前 Python 环境未安装 Agent Session Commit，仓库的 Agent、来源、工作目录和 hooks 路径均未配置；本轮只核验状态，尚未配置自动会话归档。Q2 实现与本地验证已完成，提交前仍需处理归档配置。

### Q1、Q2 最终运行自检（2026-11-07）

用户要求最后确认能否跑通。以本地 HEAD `b5866a7` 为基础检查，开始时工作区干净，本轮没有改动源码。

重新用 `g++ -std=c++17 -Wall -Wextra -pedantic -Werror` 编译 Q1、Q2 原文件及两个本地 C++ 测试文件，四次编译和四次运行退出码均为 0，没有编译警告。运行结果如下：

- Q1、Q2 原文件各输出 `PUBLIC 2/2`。
- Q1 本地测试通过 25 项定向检查及 5350 组穷举。
- Q2 本地测试通过 25 项定向检查。
- 重新运行 `python -X utf8 local_tests/q2_validation.py`，3 组规模边界及 1000 组随机序列对照全部通过。
- 运行 `python -X utf8 tools/check.py . --only q1 q2 --output scores/final-check-q1-q2`，Q1、Q2 各通过 2/2 可见组，退出码为 0。

已核对新生成报告中的源码哈希与当前文件一致。验证范围为 Q1、Q2；其余题目仍未实现。本轮只更新本记录。

### Q3 MVP（2026-11-07）

按用户要求实现 [A1_q3.cpp](../src/main/A1_q3.cpp) 中的 `alarms`，只修改实现区。新增 [q3_mvp_test.cpp](q3_mvp_test.cpp)，保留 Q1、Q2 的源码和测试。

先检查 `k`。无效时直接返回空序列，避免构造不完整窗口或用负下标访问。窗口有效时计算第一组 k 个元素的和，判断并记录右端下标 `k-1`。之后右端每前进一次，减去 `values[right-k]`，加上 `values[right]`，仅在总和严格大于阈值时记录 `right`。

总和使用 `long long`，最大绝对值为 `200000 × 10^9 = 2 × 10^14`，在其表示范围内。输入通过 const 引用传入，函数无共享可变状态。每个元素最多加入、移出各一次，时间 O(n)，返回结果以外的工作空间 O(1)。

20 项本地检查覆盖空输入、零和负 k、k 超长、int 极端 k、阈值相等、全负数、k=1、k=n、零窗口和、32 位整数无法保存的总和、正负极端阈值及输入不变。公开自检和仓库检查器均通过 2/2。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q3.cpp -o local_tests/build/q3_public.exe
.\local_tests\build\q3_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q3_mvp_test.cpp -o local_tests/build/q3_mvp_test.exe
.\local_tests\build\q3_mvp_test.exe
python -X utf8 tools/check.py . --only q3 --output scores/q3-mvp
```

运行输出依次为 `PUBLIC 2/2`、`Q3 MVP tests passed (20 checks)`、`.: auto=6.0/60 bonus=0/20`，编译和运行退出码均为 0，无编译警告。检查器仅评测 Q3 的可见组，原始权重得分 10/10；报告保存在忽略目录 `scores/q3-mvp/`，已核对源码哈希与当前文件一致。

本轮未发现功能缺陷。最大 n 的运行和独立随机序列对照尚未开展，可在后续完成 Q3 时补充。本轮没有执行 Git 提交或推送。

### Q3 最小能力边界（2026-11-07）

本轮将“最小能力边界”解释为 MVP 必须满足的完整公开契约及最低本地验收标准，保留现有滑动窗口算法。

| 能力项 | 最低要求 | 依据或验证 |
| --- | --- | --- |
| 规模与数值 | n 为 0..200000，元素为正负 10^9 以内，阈值为正负 10^15 以内 | 正式题面；定向检查和最大 n 测试 |
| 无效窗口 | k 为任意 int；k<1、k>n 或空输入均返回空序列，不访问不存在的元素 | 20 项定向检查包含负 k、零、超长和 int 极值 |
| 判定与端点 | 只处理长度恰好为 k 的连续窗口，使用严格大于，支持 k=1、k=n、负数与零 | 定向检查及最大规模的相等边界 |
| 输出 | 从 0 开始的右端下标，升序、不重复；有效 k 的输出最多 n-k+1 个 | 返回 200000 个下标及 100001 个重叠窗口，逐项核对 |
| 整数安全 | 窗口和用 long long，绝对值最大 2×10^14 | 最大正、负窗口和及阈值恰好相等测试 |
| 时间与空间 | O(n) 时间、O(1) 额外工作空间，输出空间另计 | 首窗口循环与滑动循环的迭代次数合计为 n；只保存固定数量的工作变量 |
| 输入和状态 | 输入保持不变，多次调用独立，只通过参数和返回值交互 | const 引用、无全局可变状态及输入不变检查 |

最低本地验收标准为公开自检及检查器各通过 2/2、20 项定向检查通过、8 组最大规模测试通过，且解答修改限于实现区。当前已满足这些条件；独立随机对照可作为下一轮增强验证。

新增 [q3_boundary_test.cpp](q3_boundary_test.cpp)，包含 8 组 n=200000 的规模测试：最大正负窗口和的相等与严格大于情况、k=1 的最大输出、k=100000 的大量重叠窗口，以及正负大数交替抵消。对有报警的结果逐项比较全部下标。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q3_boundary_test.cpp -o local_tests/build/q3_boundary_test.exe
.\local_tests\build\q3_boundary_test.exe
```

编译无警告，运行输出 `Q3 boundary tests passed (8 cases, n=200000, max output=200000)`，退出码为 0。本轮未修改解答源码，先前公开测试报告的源码哈希继续适用。

超出题面规定范围的 n、元素或阈值没有约定验收行为。本轮不增加相关异常或输入校验；无效 k 的明确规则仍完整支持。随机对照、教师隐藏测试和正式收卷状态尚未验证。

### Q3 完成与本地验收（2026-11-07）

用户要求完成 Q3。本轮保留现有解答源码，新增 [q3_validation.py](q3_validation.py)，用 Python 对每个完整窗口重新调用 `sum` 计算参考结果，再与 C++ 保存实现返回的下标逐项比较。

随机种子为 2627，共 1000 组输入，长度为 0～100。数据包含零、正负小整数和正负 10^9 的整数，k 包含合法窗口以及零、负数、超长和 int 极端值。阈值覆盖正负 10^15，以及抽取窗口和的相等、减一、加一情形。该参考方法没有复用滑动更新逻辑，1000 组结果全部一致。

最终重新编译并运行 Q3 原文件、20 项定向检查和 8 组最大规模测试，均通过。直接编译均使用 C++17 和 `-Wall -Wextra -pedantic -Werror`，无警告，编译及运行退出码均为 0。

最终复现命令（在仓库根目录执行，已有 `local_tests/build/`）：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q3.cpp -o local_tests/build/q3_public.exe
.\local_tests\build\q3_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q3_mvp_test.cpp -o local_tests/build/q3_mvp_test.exe
.\local_tests\build\q3_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q3_boundary_test.cpp -o local_tests/build/q3_boundary_test.exe
.\local_tests\build\q3_boundary_test.exe
python -X utf8 local_tests/q3_validation.py
python -X utf8 tools/check.py . --only q3 --output scores/q3-final
```

实际输出包括 `PUBLIC 2/2`、`Q3 MVP tests passed (20 checks)`、`Q3 boundary tests passed (8 cases, n=200000, max output=200000)`、`Q3 validation passed: 1000 random cases (seed 2627)`。仓库检查器的 Q3 可见组通过 2/2；只评测 Q3 的功能分为 6/60，不是整份作业或正式成绩。

最终报告位于忽略目录 `scores/q3-final/`，已核对随机验证报告和检查器报告中的源码哈希与当前文件一致。没有发现需要修复的功能缺陷。Q3 实现与本地验收完成；用户逐段理解、会话归档、远程 CI 和正式提交另行跟进。

### Q4 MVP（2026-11-07）

按用户要求实现 [A1_q4.cpp](../src/main/A1_q4.cpp) 中的 `execute`，只修改原实现区。新增 [q4_mvp_test.cpp](q4_mvp_test.cpp)，原有固定类型、公开测试和 main 保持原样。

每次调用初始化 `{0,0,0}`。逐行创建 `istringstream`，识别大小写敏感的 `ADD`、`SET`、`RESET`。前两种操作提取一个 long long 参数并验证范围，再计算候选值；RESET 的候选值为 0。随后检查是否仍有尾随字段，以及候选值是否处于正负 1000000 内。全部通过才写回 value 并增加 accepted，否则只增加 rejected。

参数已验证后才参与加法，旧 value 和参数的绝对值均不超过 1000000，候选和不会超过正负 2000000。极长整数导致流提取失败时直接拒绝，不使用解析失败的值。每行只进入一次最终成功或失败分支，保持 `accepted + rejected == lines.size()`。

设 T 为全部字符串的总字符数、m 为行数、L 为最长行长度，时间 O(T + m)，空间 O(L + 1)。字符串流持有当前行的副本，因此额外空间随最长行长度增长。

25 组定向命令序列均通过；每组核对 value、accepted、rejected 和计数恒等式，另核对调用方输入保持不变。测试包括空输入、空行、未知命令、缺参数、多字段、小数或字符尾缀、操作及参数范围端点、结果越界、正负 long long 解析溢出、首尾空白、正号、前导零、非法 RESET 及失败后继续执行。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q4.cpp -o local_tests/build/q4_public.exe
.\local_tests\build\q4_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q4_mvp_test.cpp -o local_tests/build/q4_mvp_test.exe
.\local_tests\build\q4_mvp_test.exe
python -X utf8 tools/check.py . --only q4 --output scores/q4-mvp
```

输出依次为 `PUBLIC 2/2`、`Q4 MVP tests passed (25 command sequences, input unchanged)`、`.: auto=7.2/60 bonus=0/20`。编译无警告，编译和运行退出码均为 0。检查器仅评测 Q4 的 2 个可见组，原始权重得分 12/12；报告在忽略目录 `scores/q4-mvp/`。

本轮没有发现功能缺陷。后续可补充 10000 行的最大规模与独立随机对照，并完成正式 PDF 的 Q4 页复核。本轮没有执行 Git 提交或推送。

### Q4 最小能力边界（2026-11-07）

本轮对照正式 PDF 确定 MVP 的最低能力范围，保留现有解答源码。

| 能力项 | 最低要求 | 依据或验证 |
| --- | --- | --- |
| 输入规模 | 每次 0..10000 行，每行独立解析，每次调用从 0 开始 | 正式规范；空输入和 8 组各 10000 行测试 |
| 格式 | 仅区分大小写的 ADD x、SET x、RESET，参数数量严格匹配，十进制按标准流提取 | 25 组定向序列覆盖操作、参数、空白、正号、前导零及尾随内容 |
| 数值 | 参数和更新结果都在正负 1000000 内，包含端点；解析溢出拒绝 | 上下限交替越界与 10000 位越界整数测试 |
| 事务 | 完整验证后才修改 value；失败只增加 rejected，保留原值并继续处理 | 非法 RESET 连续 9999 次仍保留值；越界后 RESET 和后续 ADD 正常 |
| 计数 | 每行恰好接受或拒绝一次，accepted+rejected=lines.size() | 每组测试核对最终值、两项计数和恒等式 |
| 状态 | 不修改输入，多次调用独立；空输入返回 {0,0,0} | const 输入与输入不变检查，多组连续独立调用 |
| 时间与空间 | 总字符数 T、行数 m、最长行 L 下，O(T+m) 时间、O(L+1) 空间 | 每行扫描当前字符串，流和词元存储随当前行长度增长 |

题面没有给出单行长度上限，不额外设置字符数限制。10000 位越界整数应被拒绝；带 10000 个前导零、数值仍为 1 的合法整数应正常接受。这两种情况均已实跑通过。超过 10000 行的输入未规定验收行为；参数越界则属于题面明确要求拒绝的情况。

最低本地验收标准为公开自检及检查器各通过 2/2、25 组定向序列通过、8 组最大行数测试通过，且实现区以外的固定内容保持原样。当前满足这些条件。独立随机对照尚未开展，教师隐藏测试和正式提交状态未核验。

新增 [q4_boundary_test.cpp](q4_boundary_test.cpp)，8 组均包含 10000 行，分别检查全成功、全空行拒绝、上下限各自反复越界、非法 RESET 保留原值、连续合法 RESET、超长数字溢出后继续累加、超长合法前导零与非法尾缀混合。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q4_boundary_test.cpp -o local_tests/build/q4_boundary_test.exe
.\local_tests\build\q4_boundary_test.exe
```

编译无警告，输出 `Q4 boundary tests passed (8 batches, 10000 lines each, 10000-digit numeric fields)`，退出码为 0。本轮未修改解答源码，已核对其哈希仍与此前通过的 Q4 检查器报告一致。README 已同步能力范围和实际验证结果。

### Q4 完成与本地验收（2026-11-07）

用户要求完成 Q4。本轮保留原有解答源码，新增 [q4_validation.py](q4_validation.py)。Python 参考方法用正则表达式完整匹配命令和十进制参数，再独立执行范围检查与状态更新，不复用 C++ 的流提取逻辑。

固定随机种子为 2627，生成 1000 组、每组 0～100 行的命令序列。数据混合合法命令、正负范围端点、零、前导零、六种标准空白、缺参数、多字段、未知操作、小数与字符尾缀、解析溢出及超长数字。测试驱动用十六进制传输原始字符串，保留换行和空字符，再逐项比较最终值、成功数与拒绝数，并核对计数恒等式。1000 组全部一致。

最终重新编译并运行 Q4 原文件、25 组定向序列和 8 组各 10000 行的边界测试，全部通过。三个程序均使用 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译和运行退出码均为 0。

最终复现命令（在仓库根目录执行，已有 `local_tests/build/`）：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q4.cpp -o local_tests/build/q4_public.exe
.\local_tests\build\q4_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q4_mvp_test.cpp -o local_tests/build/q4_mvp_test.exe
.\local_tests\build\q4_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q4_boundary_test.cpp -o local_tests/build/q4_boundary_test.exe
.\local_tests\build\q4_boundary_test.exe
python -X utf8 local_tests/q4_validation.py
python -X utf8 tools/check.py . --only q4 --output scores/q4-final
```

实际输出包括 `PUBLIC 2/2`、`Q4 MVP tests passed (25 command sequences, input unchanged)`、`Q4 boundary tests passed (8 batches, 10000 lines each, 10000-digit numeric fields)`、`Q4 validation passed: 1000 random sequences (seed 2627)`。检查器仅评测 Q4，可见组通过 2/2，折合功能分 7.2/60；该分数不是整份作业成绩。

最终报告位于忽略目录 `scores/q4-final/`，已核对随机验证与检查器报告中的源码哈希和当前文件一致。未发现需要修复的解答功能缺陷。Q4 实现与本地验收完成；用户逐段理解、会话归档、远程 CI 和正式提交另行跟进。

### Q5 MVP（2026-11-07）

按用户要求实现 [A1_q5.cpp](../src/main/A1_q5.cpp) 的 `risk`，只修改原实现区。新增 [q5_mvp_test.cpp](q5_mvp_test.cpp)，保留既有题目的源码、测试和固定内容。

空地图直接返回空矩阵。非空地图先检查零列、每行长度及全部字符；零列、行长不一致或非法字符均抛出 `std::invalid_argument`。所有验证完成后才分配输出并计算风险，障碍写为 -1，空地只统计上、下、左、右四个方向中的障碍，读取邻格前先检查行列边界。

设地图为 R 行、C 列，验证和计算均为 O(RC) 时间。结果占 O(RC) 空间，逐行直接初始化输出，没有额外的整行或整图副本，返回结果以外的工作空间为 O(1)。输入通过 const 引用传入，调用独立。

20 项本地检查覆盖空地图、单格、单行、单列、全障碍、全空地、对角障碍不计、中心四邻障碍、非方形地图、零列、长短不齐、非法首字符、非法末字符及输入不变。其中 7 项核对 `std::invalid_argument` 异常类型。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q5.cpp -o local_tests/build/q5_public.exe
.\local_tests\build\q5_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q5_mvp_test.cpp -o local_tests/build/q5_mvp_test.exe
.\local_tests\build\q5_mvp_test.exe
python -X utf8 tools/check.py . --only q5 --output scores/q5-mvp
```

输出依次为 `PUBLIC 2/2`、`Q5 MVP tests passed (20 checks)`、`.: auto=7.2/60 bonus=0/20`，编译无警告，编译与运行退出码均为 0。检查器只评测 Q5 的两个可见组，原始权重得分 12/12；报告保存在忽略目录 `scores/q5-mvp/`，已核对源码哈希与当前文件一致。

正式 PDF 第 13、14 页的 Q5 规则已直接复核，与 Markdown 一致。本轮未发现功能缺陷。最大 300×300 地图和独立随机对照尚未验证，可在后续确定能力边界或完成 Q5 时补充。本轮没有执行 Git 提交或推送。

### Q5 最小能力边界（2026-11-07）

本轮对照正式题面确立 Q5 MVP 的最低能力范围，保留现有解答源码。

| 能力项 | 最低要求 | 依据或验证 |
| --- | --- | --- |
| 输入范围 | 空地图，或 1..300 行、1..300 列的矩形地图，只含点和井号 | 题面约束；单格、单行、单列及最大地图 |
| 格式异常 | 非空但零列、行长不一致或非法字符均抛出 std::invalid_argument | 7 项基础异常检查及大地图末尾非法输入 |
| 验证顺序 | 先验证全部输入，再计算风险，不返回部分结果 | 源码先完成验证循环才创建输出；最大地图最后一格或最后一行错误会抛出异常 |
| 风险含义 | 障碍为 -1，空地为上下左右障碍数 0..4，不计对角和越界位置 | 小地图定向结果及 300×300 棋盘格逐格核验 |
| 输出与状态 | 同尺寸、同行列顺序，输入不变，调用独立 | 形状检查、完整矩阵比较、const 输入及基础输入不变检查 |
| 时间与空间 | O(RC) 时间、O(RC) 结果空间，结果以外 O(1) 工作空间 | 验证和计算各遍历地图，每格检查最多四个邻格，直接逐行填充返回矩阵 |

300 行和 300 列是题面给出的输入范围上限。更大地图的处理不列入本轮能力承诺；零列、行长不一致和非法字符的明确异常规则完整支持。

最低本地验收标准为公开自检及检查器各通过 2/2、20 项基础检查通过、8 组规模边界通过，且只在实现区修改解答。当前满足这些条件。独立随机对照尚未开展，教师隐藏测试和正式提交状态未核验。

新增 [q5_boundary_test.cpp](q5_boundary_test.cpp)，8 组覆盖 300×300 全空地图、全障碍地图、棋盘格地图、300 格单行、300 格单列、最大地图最后一个字符非法、最后一行长度少一格和 300 个零列空行。三个最大合法矩阵共逐格核对 270000 个结果格，单行和单列也比较完整矩阵。

实际运行命令：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q5_boundary_test.cpp -o local_tests/build/q5_boundary_test.exe
.\local_tests\build\q5_boundary_test.exe
```

编译无警告，输出 `Q5 boundary tests passed (8 cases, max 300x300, 90000 cells)`，退出码为 0。本轮未修改解答源码，已核对其哈希与此前通过的 Q5 检查器报告一致。README 已同步能力清单和实际结果。

### Q5 完成与本地验收（2026-11-07）

用户要求完成 Q5。本轮保留原有解答源码，新增 [q5_validation.py](q5_validation.py)。参考方法先验证格式，再从每个障碍向四周空地累加风险，与 C++ 逐个空地统计障碍的方法分开实现。

固定随机种子为 2627，共 1000 组地图，尺寸不超过 20 行、20 列。750 组合法地图包含空地图，对输出行列数和每个格子的风险值完整比较；250 组非法地图包括零列、行长不一致以及非法字符，测试驱动只将 `std::invalid_argument` 识别为预期失败。字符串用十六进制传输，保留空字符串、换行和空字符。1000 组结果全部与参考方法一致。

最终重新编译并运行 Q5 原文件、20 项定向检查和 8 组规模边界，全部通过。三个程序均使用 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译和运行退出码均为 0。

最终复现命令（在仓库根目录执行，已有 `local_tests/build/`）：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q5.cpp -o local_tests/build/q5_public.exe
.\local_tests\build\q5_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q5_mvp_test.cpp -o local_tests/build/q5_mvp_test.exe
.\local_tests\build\q5_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q5_boundary_test.cpp -o local_tests/build/q5_boundary_test.exe
.\local_tests\build\q5_boundary_test.exe
python -X utf8 local_tests/q5_validation.py
python -X utf8 tools/check.py . --only q5 --output scores/q5-final
```

实际输出包括 `PUBLIC 2/2`、`Q5 MVP tests passed (20 checks)`、`Q5 boundary tests passed (8 cases, max 300x300, 90000 cells)`、`Q5 validation passed: 1000 random maps (750 valid, 250 invalid, seed 2627)`。检查器仅评测 Q5，可见组通过 2/2，折合功能分 7.2/60；该分数不是整份作业成绩。

最终报告位于忽略目录 `scores/q5-final/`，已核对随机验证与检查器报告中的源码哈希与当前文件一致。未发现需要修复的解答功能缺陷。Q5 实现与本地验收完成；用户逐段理解、会话归档、远程 CI 和正式提交另行跟进。

### Q6 MVP（2026-11-07）

用户要求 Q6 MVP。本轮核对正式 PDF 第 15、16 页（页脚 14、15）的接口、六条规范及三个样例，与 Markdown 一致。解答只修改 [A1_q6.cpp](../src/main/A1_q6.cpp) 的实现区，新增 [q6_mvp_test.cpp](q6_mvp_test.cpp)，同步 README 和本记录。

算法先处理负射程，然后逐个目标筛选 `visible && hp>0`，用平方距离判断是否在含边界的射程内。保留当前最佳编号、血量和平方距离，按血量、距离、编号依次更新。编号非负，所以用 -1 表示无候选。整个过程不排序或修改输入，也不保留跨调用状态。

坐标提升到 `long long` 后才相乘；射程平方使用 `1LL * max_range * max_range`。坐标绝对值不超过 10^6，平方距离最大为 2×10^12；射程平方最大为 10^12，均在 64 位整数范围内。时间 O(n)，额外空间 O(1)。

30 项本地检查覆盖三种淘汰条件、负射程及 int 最小负值、空输入、三级优先级、编号 0 与 int 最大编号、零射程、负坐标、射程边界、百万级坐标、32 位乘法溢出风险、输入顺序与字段保持、逆序后的相同选择以及独立调用。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q6.cpp -o local_tests/build/q6_public.exe
.\local_tests\build\q6_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q6_mvp_test.cpp -o local_tests/build/q6_mvp_test.exe
.\local_tests\build\q6_mvp_test.exe
python -X utf8 tools/check.py . --only q6 --output scores/q6-mvp
```

输出依次为 `PUBLIC 2/2`、`Q6 MVP tests passed (30 checks)`、`.: auto=8.4/60 bonus=0/20`，编译和运行退出码均为 0，无编译警告。检查器只评测 Q6，可见组 2/2，原始权重得分 14/14；8.4/60 是本题折合公开功能分，不是整份作业成绩。报告保存在忽略目录 `scores/q6-mvp/`，源码哈希已核对一致。

本轮未发现功能缺陷。10 万目标的最大规模运行和独立随机对照尚未开展，后续确定能力边界与完成 Q6 时补充。此前版本控制优化文件继续保留，未暂存、提交或推送。

### Q6 最小功能边界（2026-11-07）

本轮以正式题面的六条规范确定 MVP 必须满足的最小功能范围。再次提取 PDF 第 15 页核对规范，保留现有解答源码。

| 能力项 | 最低要求 | 依据与验证 |
| --- | --- | --- |
| 规模与数值 | 目标数为 0..100000；id 非负且唯一；坐标绝对值不超过 10^6，hp 为 -100..100 | 正式规范；30 项定向检查与 8 组最大规模测试 |
| 射程与空输入 | max_range<0 直接返回 -1；有效范围 0..10^6；空输入返回 -1 | 已测负射程、int 最小负值、空输入和零射程 |
| 资格与端点 | visible=true、hp>0、x²+y²≤max_range² 同时成立才参与比较 | 定向测试及最大规模全淘汰、混合淘汰、精确射程边界 |
| 三级优先级 | 依次比较 hp、平方距离、id，均取小者；平局后才使用下一级 | 末尾最低血量、末尾最近目标、10 万个目标编号正逆序平局 |
| 输出 | 返回目标 id，无候选返回 -1 | 胜出编号 99999 位于末尾；所有目标淘汰时返回 -1 |
| 整数安全 | 平方与求和都以 64 位整数计算，平方距离最大 2×10^12 | 百万级正负坐标、全在圆外及 (-600000,±800000) 精确边界 |
| 资源 | O(n) 时间、O(1) 额外空间 | 单次循环、固定数量工作变量，不排序、不复制输入；最大规模实跑通过 |
| 输入与状态 | 输入不变、排列顺序不影响选择、每次调用独立 | 每组规模测试逐字段核对原副本；编号正逆序结果一致；定向检查覆盖调用独立性 |

除明确规定的负射程外，验收输入遵循题面保证；不额外要求重复编号、坐标越界等未规定输入的异常处理。函数只通过参数和返回值交互。

最低本地验收标准为公开自检及检查器各通过 2/2、30 项定向检查通过、8 组各 100000 目标的规模测试通过，且解答只改实现区。当前已满足。独立随机对照留待后续完成 Q6 时补充，远程 CI 与正式评分未核验。

新增 [q6_boundary_test.cpp](q6_boundary_test.cpp)，8 组分别为全不可见、全血量不大于零、全超射程、末尾目标血量最小、末尾目标距离最近、编号降序平局、编号升序平局，以及混合淘汰后仅末尾目标合格。每组均有 100000 个非负且唯一的编号，结果预先由构造确定，并逐字段确认输入保持不变。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q6_boundary_test.cpp -o local_tests/build/q6_boundary_test.exe
.\local_tests\build\q6_boundary_test.exe
```

输出 `Q6 boundary tests passed (8 cases, n=100000 each)`，编译无警告，编译与运行退出码均为 0。本轮未改动解答，已核对源码 SHA256 与此前通过的 Q6 MVP 检查器报告一致，未重复运行无变化的公开测试。

本轮开始时已发现用户新提交 `d995ef8`，同时包含 Q6 MVP、此前版本控制优化文件和首个 bundle。已验证该 bundle 可完整读取，其中两份真实文字导出共 122 条消息，导出哈希与清单一致；这证明首包已入库，不表示遗漏内容和教师认可范围已全部核定。助手本轮没有执行提交、推送或改写历史。

### Q6 完成与本地验收（2026-11-07）

用户要求完成 Q6。本轮保留现有解答，新增 [q6_validation.py](q6_validation.py)。参考方法使用 Python 任意精度整数筛选候选，然后对 `(hp, distance_squared, id)` 排序取首项，与 C++ 保留当前最佳值的单次遍历分开实现。

随机种子为 2627，共 1000 组输入。八类各 125 组，分别覆盖宽范围随机数据、血量优先、距离优先、编号平局、射程边界与仅超出平方距离 1、负射程、零射程及全部淘汰。其中 628 组有合格目标，372 组无候选。编号非负且唯一，包含 0 和 int 最大值；坐标、血量与射程均核对符合题面范围。

每组分别按原序、逆序和固定种子随机重排运行，共 3000 次 C++ 调用、2000 项顺序不变性检查；每次调用后逐字段确认输入不变。所有结果均与参考编号一致。单个驱动依次处理全部调用，也覆盖了不同输入连续调用的独立性。

本轮重新编译并运行原文件、30 项定向检查和 8 组最大规模检查，全部通过。三个常驻程序及临时随机驱动均以 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译与运行退出码均为 0。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q6.cpp -o local_tests/build/q6_public.exe
.\local_tests\build\q6_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q6_mvp_test.cpp -o local_tests/build/q6_mvp_test.exe
.\local_tests\build\q6_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q6_boundary_test.cpp -o local_tests/build/q6_boundary_test.exe
.\local_tests\build\q6_boundary_test.exe
python -X utf8 -B local_tests/q6_validation.py
python -X utf8 tools/check.py . --only q6 --output scores/q6-final
```

实际输出包括 `PUBLIC 2/2`、`Q6 MVP tests passed (30 checks)`、`Q6 boundary tests passed (8 cases, n=100000 each)`、`Q6 validation passed: 1000 random cases, 3000 calls, 2000 permutation checks (seed 2627)`。检查器仅评测 Q6，可见组 2/2，原始权重得分 14/14，折合公开功能分 8.4/60；该分数不是整份作业成绩。

最终报告位于忽略目录 `scores/q6-final/`，随机验证与检查器报告中的源码哈希已与当前文件核对一致。未发现需要修复的功能缺陷，解答源码保持不变。Q6 实现与本地验收完成；用户逐段理解、后续增量归档、远程 CI 和正式提交另行跟进。本轮未暂存、提交或推送。

### Q7 MVP（2026-11-07）

用户要求 Q7 MVP。本轮核对正式 PDF 第 17、18 页（页脚 16、17）的接口、六条规范与三个样例，与 Markdown 一致。只修改 [A1_q7.cpp](../src/main/A1_q7.cpp) 的实现区，新增 [q7_mvp_test.cpp](q7_mvp_test.cpp)，同步 README 和本记录。

算法使用本次调用的 `FireResult{0,0,ammo,heat}` 保存状态。每帧先执行 `max(0, heat-cool)`；请求为 0 时进入下一帧，请求为 1 时检查剩余弹量和加热后是否超过 100。成功时扣弹、加热并计数；失败只增加拒绝次数，已发生的冷却保留。空请求直接返回初始状态，不发生额外冷却。

设请求数为 n，时间 O(n)、额外空间 O(1)。输入参数均在 0..100，热量加法最多为 200；n≤10000，两个计数最多为 10000，int 足够。输入请求只读，无全局可变状态，每次调用独立。

30 项定向检查覆盖公开样例、空请求、冷却归零、先冷却再判断、热量恰为 100 与超过 1、拒绝保留冷却、无弹、零冷却、零射击热量、拒绝后恢复、弹量耗尽和调用独立性。每次结果核对四个字段，同时检查 `shots+rejected=count(requests==1)`、`ammo=initial_ammo-shots`、热量范围和请求输入不变。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q7.cpp -o local_tests/build/q7_public.exe
.\local_tests\build\q7_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q7_mvp_test.cpp -o local_tests/build/q7_mvp_test.exe
.\local_tests\build\q7_mvp_test.exe
python -X utf8 tools/check.py . --only q7 --output scores/q7-mvp
```

输出依次为 `PUBLIC 2/2`、`Q7 MVP tests passed (30 checks)`、`.: auto=9.6/60 bonus=0/20`，编译和运行退出码均为 0，无编译警告。检查器只评测 Q7，可见组通过 2/2，原始权重得分 16/16；9.6/60 是本题折合公开功能分，不是整份作业成绩。报告保存在忽略目录 `scores/q7-mvp/`，源码哈希已核对一致。

本轮未发现功能缺陷。10000 帧的最大规模与独立随机对照尚未开展，可在后续确定最小能力边界、完成 Q7 时补充。本轮未暂存、提交或推送。

### Q7 最低功能边界（2026-11-07）

本轮依据正式题面六条规范确认 MVP 的最低能力范围，再次提取 PDF 第 17 页核对规范，保留现有解答源码。

| 能力项 | 最低要求 | 依据与验证 |
| --- | --- | --- |
| 输入范围 | 请求数为 0..10000，元素为 0 或 1；ammo、heat、cool、shot_heat 均为 0..100 | 正式规范；30 项定向检查与 8 组最大规模测试 |
| 冷却与顺序 | 每帧先计算 max(0,heat-cool)，包括空闲、无弹和过热帧 | 定向测试及连续拒绝、交替请求、每百帧射击测试 |
| 空闲请求 | 请求为 0 只冷却，不扣弹、不增加任一计数 | 全空闲 10000 帧保持弹量，计数均为 0 |
| 发射判定 | 请求为 1，ammo>0 且冷却后 heat+shot_heat≤100 才成功 | 端点 100、零射击热量、最大冷却和射击热量均覆盖 |
| 成功与拒绝 | 成功扣一弹、加射击热量、shots 加一；拒绝只增加 rejected，保留已发生冷却 | 持续过热、无弹、拒绝后恢复及耗尽弹量后的继续冷却 |
| 空序列与状态 | 空序列返回原始 ammo、heat 和零计数；输入不变，每次调用独立 | 定向检查与每组规模测试的输入副本比较 |
| 守恒与数值 | shots+rejected=count(requests==1)，ammo+shots=initial_ammo；heat 保持 0..100 | 每组规模测试均核对；shots≤100、rejected≤10000，加热判定最多 200，int 足够 |
| 资源 | O(n) 时间、O(1) 额外空间 | 单次循环和固定大小结果对象；10000 帧实跑通过 |

最低验收输入遵循题面保证；超范围参数和非 0/1 请求不在最低功能范围内。函数只通过参数和返回值交互。

最低本地验收标准为公开自检及检查器各通过 2/2、30 项定向检查通过、8 组各 10000 帧的规模测试通过，且解答只修改实现区。当前已满足。独立随机对照留待完成 Q7 时补充，远程 CI 与正式评分未核验。

新增 [q7_boundary_test.cpp](q7_boundary_test.cpp)，8 组分别为全空闲、无弹持续请求、无冷却持续过热、零射击热量、最大冷却与加热、每百帧恢复射击、射击与空闲交替、仅最后一帧请求。每组核对全部四个返回字段、请求计数、弹量守恒、热量范围与输入不变。

关键预期由序列构造确定：10000 次无弹请求全部拒绝；100 发子弹、零射击热量时成功 100 次、拒绝 9900 次；初热量 100、cool=1、shot_heat=100 的连续请求，每 100 帧成功一次，最后一帧恰好是第 100 次射击，末态热量 100；最大冷却情况下耗尽弹量后继续冷却，末态热量为 0。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q7_boundary_test.cpp -o local_tests/build/q7_boundary_test.exe
.\local_tests\build\q7_boundary_test.exe
```

输出 `Q7 boundary tests passed (8 cases, 10000 frames each)`，编译无警告，编译与运行退出码均为 0。本轮未改动解答，已核对其源码哈希与此前通过的 Q7 MVP 检查器报告一致，未重复运行无变化的公开测试。本轮测试与文档未暂存、提交或推送。

### Q7 完成与本地验收（2026-11-07）

用户要求完成 Q7。本轮保留现有解答，新增 [q7_validation.py](q7_validation.py)。参考模型在两次射击请求之间累计冷却，逐个记录实际成功事件；从事件数与请求总数推导 shots、rejected 和剩余弹量，最后补算末次请求后的空闲冷却。它与 C++ 的逐帧状态更新分开实现，空序列不会发生冷却。

固定随机种子为 2627，共 1000 组输入。八类各 125 组，分别为混合请求、参数端点、空闲或空序列、无弹、零冷却、零射击热量、热量上限附近和稀疏请求。其中 10 组达到 10000 帧，其余不超过 200 帧；全部参数、请求值和分割位置已核对符合题面范围。

每组分别运行整段、前半段和后半段，共 3000 次 C++ 调用。后半段从实际前半段的剩余弹量、热量继续；两段计数相加、末态取后半段，必须与整段四字段一致。共 1000 项分段衔接检查通过，分割位置包括空前段、空后段和序列中间。全部 3000 次结果也逐字段与独立参考核对，每次调用的请求输入均保持不变。

本轮重新编译并运行原文件、30 项定向检查和 8 组万帧规模检查，全部通过。三个常驻程序及临时随机驱动均以 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译与运行退出码均为 0。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q7.cpp -o local_tests/build/q7_public.exe
.\local_tests\build\q7_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q7_mvp_test.cpp -o local_tests/build/q7_mvp_test.exe
.\local_tests\build\q7_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q7_boundary_test.cpp -o local_tests/build/q7_boundary_test.exe
.\local_tests\build\q7_boundary_test.exe
python -X utf8 -B local_tests/q7_validation.py
python -X utf8 tools/check.py . --only q7 --output scores/q7-final
```

实际输出包括 `PUBLIC 2/2`、`Q7 MVP tests passed (30 checks)`、`Q7 boundary tests passed (8 cases, 10000 frames each)`、`Q7 validation passed: 1000 random cases, 3000 calls, 1000 continuation checks (10 cases with 10000 frames, seed 2627)`。检查器仅评测 Q7，可见组 2/2，原始权重得分 16/16，折合公开功能分 9.6/60；该分数不是整份作业成绩。

最终报告位于忽略目录 `scores/q7-final/`，随机验证与检查器报告中的源码哈希已与当前文件核对一致。未发现需要修复的功能缺陷，解答源码保持不变。Q7 实现与本地验收完成；用户逐段理解、后续增量归档、远程 CI 和正式提交另行跟进。本轮未暂存、提交或推送。

### Q8 MVP（2026-11-07）

用户要求 Q8 MVP。本轮核对正式 PDF 第 19、20 页（页脚 18、19）的接口、七条规范和两个样例，与 Markdown 一致。只修改 [A1_q8.cpp](../src/main/A1_q8.cpp) 的实现区，新增 [q8_mvp_test.cpp](q8_mvp_test.cpp)，同步 README 和本记录。

算法使用本次调用的 `Summary{0,0,0,0,{}}` 和 10000 项布尔标记表。先检查 id 与 hp 两个字段是否完整合法，非法则增加 invalid 并进入下一条；合法后才访问标记表、判定重复。首次合法记录设置标记、增加 valid，将血量夹到 0..100 后累加；重复合法记录只增加 duplicate。最后扫描整个编号域生成升序 ids。

输入字段可以是任意 int，比较范围后才作数组索引，避免负编号和极大编号越界。血量接收范围 -1000..1000 与累计夹取范围 0..100 分开处理。total_hp 使用 long long，最多 10000 个不同编号各贡献 100，总和不超过 1000000。分类计数最多为 20000，int 足够。

设 n 为输入记录数、U=10000 为编号域大小、k 为首次合法编号数，初始化和扫描标记表均为 O(U)，总时间 O(n+U)，额外工作空间 O(U)，返回 ids 另占 O(k)。输入只读，标记与结果每次重新初始化，不依赖其他题。

32 项定向检查覆盖公开样例、空输入、编号与血量范围端点、两个字段的 int 极值、合法负血量、夹取端点、首次合法值保留、非法后补发、已见编号的非法记录、双字段同时非法只计一次、乱序编号、输入不变和连续调用。每项核对全部五个返回字段、分类计数恒等式、valid=ids.size()、总血量范围和编号升序且唯一。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q8.cpp -o local_tests/build/q8_public.exe
.\local_tests\build\q8_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q8_mvp_test.cpp -o local_tests/build/q8_mvp_test.exe
.\local_tests\build\q8_mvp_test.exe
python -X utf8 tools/check.py . --only q8 --output scores/q8-mvp
```

输出依次为 `PUBLIC 2/2`、`Q8 MVP tests passed (32 checks)`、`.: auto=10.8/60 bonus=0/20`，编译和运行退出码均为 0，无编译警告。检查器只评测 Q8，可见组通过 2/2，原始权重得分 18/18；10.8/60 是本题折合公开功能分，不是整份作业成绩。报告保存在忽略目录 `scores/q8-mvp/`，源码哈希已核对一致。

本轮未发现功能缺陷。20000 条记录的最大规模和独立随机对照尚未开展，可在后续确定最低功能边界、完成 Q8 时补充。本轮未暂存、提交或推送。

### Q8 最小能力边界（2026-11-07）

本轮依据正式题面七条规范确认 MVP 的最低能力范围，再次提取 PDF 第 19、20 页核对规范，保留现有解答源码。

| 能力项 | 最低要求 | 依据与验证 |
| --- | --- | --- |
| 输入范围与安全 | n 为 0..20000，id、hp 可为任意 int；先验证编号再访问标记表 | 正式规范；32 项定向检查、最大规模全极值非法输入 |
| 完整合法性 | 仅 id∈[0,9999] 且 hp∈[-1000,1000] 时合法；非法不占编号 | 定向端点检查与 10000 个编号的非法后补发 |
| 分类顺序 | 完整验证后才判重复，已见编号的非法记录仍计 invalid | 10000 条首次合法后再收到 10000 条非法血量，duplicate 为 0 |
| 首次与累计 | 首次合法记录计 valid，hp 夹到 [0,100] 后累加；合法重复只增加 duplicate | 全编号先正后负保留最大总量，先负后正保留零贡献 |
| 编号清单 | ids 升序且唯一，最多 10000 项，valid=ids.size() | 反序覆盖全部编号，完整清单逐项比较 0..9999 |
| 分类守恒 | valid+duplicate+invalid=n，每条记录恰属一类 | 每组规模测试核对全部统计与恒等式；混合批次三类均出现 |
| 数值范围 | 三类计数不超过 20000；total_hp 使用 long long，总量不超过 1000000 | 全编号首次血量 1000，累计恰为 1000000 |
| 空输入与状态 | 空输入计数、总量为 0，ids 为空；输入不变，调用独立，不依赖其他题 | 定向连续调用；所有规模批次逐字段比较输入副本 |
| 资源 | 当前路线为 O(n+U) 时间、O(U) 工作空间，U=10000；输出另占 O(k) | 标记表初始化、输入遍历、编号域扫描；最大规模实跑通过 |

最低本地验收标准为公开自检及检查器各通过 2/2、32 项定向检查通过、8 组各 20000 条记录的规模测试通过，并完整核对最大编号清单与总量，且解答只修改实现区。当前已满足。独立随机对照留待完成 Q8 时补充，远程 CI 与正式评分未核验。

新增 [q8_boundary_test.cpp](q8_boundary_test.cpp)，8 组分别为全非法 int 极值、同一合法编号重复 20000 次、全编号先最大血量后负血量、全编号先负血量后最大血量、全编号非法后补发、已见编号再收到非法血量、5000 个编号的四条记录混合分类，以及仅最后一条合法。每组均为 20000 条输入，核对全部五个返回字段、完整 ids、分类计数和输入不变。

关键预期由构造确定：全非法计 invalid=20000；同编号合法重复计 valid=1、duplicate=19999；全编号覆盖时 ids 为 0..9999，最大总量为 1000000；首次合法血量为 -1000 时总量为 0，后续合法重复不覆盖；混合批次 valid=5000、duplicate=5000、invalid=10000，总量为 500000。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q8_boundary_test.cpp -o local_tests/build/q8_boundary_test.exe
.\local_tests\build\q8_boundary_test.exe
```

输出 `Q8 boundary tests passed (8 cases, 20000 records each, 10000 legal IDs)`，编译无警告，编译与运行退出码均为 0。本轮未改动解答，已核对其源码哈希与此前通过的 Q8 MVP 检查器报告一致，未重复运行无变化的公开测试。本轮测试与文档未暂存、提交或推送。

本轮开始时，用户已将 MVP 提交为 `3545076`，本地跟踪记录显示 main 领先保存的 origin/main 1 个提交。该状态未联网刷新，不能替代 GitHub 上的最终同步或 CI 核对。

### Q8 完成与本地验收（2026-11-07）

用户要求完成 Q8。本轮新增 [q8_validation.py](q8_validation.py)。参考模型先筛选完整合法记录，再按编号稳定排序、分组，读取每组第一条血量，计算夹取后的贡献；valid 为组数，duplicate 为合法条数减组数，invalid 为总条数减合法条数。它与 C++ 标记表逐条分类及编号扫描分开实现。

固定随机种子为 2627，共 1000 组输入。八类各 125 组，分别为混合字段、字段端点、密集重复、非法后合法、合法后非法、合法负血量、唯一乱序编号和全非法。包含任意 int 范围内的极值字段；原批次最多 10000 条，整批重复后最多 20000 条，共有 10 组达到该上限。

每组运行原序、逆序、整批重复及空批次，共 4000 次 C++ 调用。逆序独立计算参考，不假设总血量不变；其中 361 组因首条合法值变化而改变总量，结果均与参考一致。整批重复应保持 valid、total_hp 和 ids，将 invalid 变为原值两倍、duplicate 变为 `2*duplicate+valid`；1000 项检查均通过。空批次重置检查 1000 项通过，所有调用后核对输入不变，全部统计与完整编号清单均和参考一致。

本轮重新编译并运行原文件、32 项定向检查、8 组两万条规模检查，全部通过。三个常驻程序及临时随机驱动均以 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译和运行退出码均为 0。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_q8.cpp -o local_tests/build/q8_public.exe
.\local_tests\build\q8_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q8_mvp_test.cpp -o local_tests/build/q8_mvp_test.exe
.\local_tests\build\q8_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/q8_boundary_test.cpp -o local_tests/build/q8_boundary_test.exe
.\local_tests\build\q8_boundary_test.exe
python -X utf8 -B local_tests/q8_validation.py
python -X utf8 tools/check.py . --only q8 --output scores/q8-final
python -X utf8 tools/check.py . --output scores/assessment-core-final --require-core
```

Q8 输出包括 `PUBLIC 2/2`、`Q8 MVP tests passed (32 checks)`、`Q8 boundary tests passed (8 cases, 20000 records each, 10000 legal IDs)`、`Q8 validation passed: 1000 random cases, 4000 calls, 1000 doubled-batch checks, 1000 empty resets (10 batches with 20000 records, seed 2627)`。Q8 专项检查可见组 2/2，原始权重 18/18，折合公开功能分 10.8/60。

完整检查输出 `.: auto=60.0/60 bonus=0.0/20`，`--require-core` 退出码为 0。Q1–Q8 各通过 2/2，共 16/16；B1、B2 仍为模板，各 0/2，不影响仅要求必做题的退出码。人工分待评，正式评分使用教师私有测试，远程 CI 与交卷状态尚未核验。

专项报告位于忽略目录 `scores/q8-final/`，完整报告在 `scores/assessment-core-final/`。已核对随机、专项及完整报告中的 Q8 源码哈希一致，完整报告的十个源码哈希也均与当前文件一致。运行期间观察到 Q1–Q8 各有一行注释删除差异，函数逻辑未变；助手未修改这些源文件，保留了工作区改动，报告对应当前磁盘版本。

未发现需要修复的解答功能缺陷。Q8 与全部必做题本地验收完成；用户逐段理解、后续增量归档、远程 CI 和正式提交另行跟进。本轮未暂存、提交或推送。

### B1 MVP（2026-11-07）

用户要求 B1 MVP，已确认开始此选做题。本轮核对正式 PDF 第 21、22 页（页脚 20、21）的接口、六条规范与样例，与 Markdown 一致。只修改 [A1_b1.cpp](../src/main/A1_b1.cpp) 的实现区，新增 [b1_mvp_test.cpp](b1_mvp_test.cpp)，同步 README、本记录与提交指南中的报告时间范围说明。

算法先检查空串、可选正负号及符号后的数字是否存在。逐字符要求 ASCII '0'..'9'，用局部 long long 累计绝对值。正数限值为 2147483647，负数为 2147483648；每次乘 10 并加数字前先检查 `value > (limit-digit)/10`，超限直接失败。全部合法后再以 long long 应用负号、转换为 int，并一次性写入 output。

该检查保证下一次乘加结果不超过对应限值，既保护 1000 位输入，也允许长前导零；最小负数不需要在 int 中取绝对值或取反。没有调用 stoi/stol/stoll、字符串流或 C 转换函数，也没有自定义 class。时间 O(n)，额外空间 O(1)，输入文本只读；所有失败路径均位于写回之前。

44 项定向检查覆盖正负零、前导零、正负范围端点及越界一位、空串和单独符号、空白、多符号、指数与十六进制格式、内嵌空字符、非 ASCII 字节、全角数字及 U+0661 的 UTF-8 字节串、64 位量级溢出、1000 位零串与溢出串。失败测试核对初始 output 的保留，包含 int 最小值和最大值；连续调用复现正式样例中的成功、失败与再次成功。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_b1.cpp -o local_tests/build/b1_public.exe
.\local_tests\build\b1_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/b1_mvp_test.cpp -o local_tests/build/b1_mvp_test.exe
.\local_tests\build\b1_mvp_test.exe
python -X utf8 tools/check.py . --only b1 --output scores/b1-mvp
```

输出依次为 `PUBLIC 2/2`、`B1 MVP tests passed (44 checks)`、`.: auto=0.0/60 bonus=10.0/20`，编译和运行退出码均为 0，无编译警告。检查器仅评测 B1，可见组通过 2/2，公开选做分为 10/20；本次 auto=0 由仅选择 B1 产生，不表示已完成的必做题失分。专项报告保存在忽略目录 `scores/b1-mvp/`，源码哈希已核对一致。

本轮未发现功能缺陷。后续可确认最小能力边界，补充最大长度的符号、补零、末尾非法字符组合及独立随机对照。B1 改动不涉及已验收的 Q1–Q8；此前完整报告反映 B1 开始前的版本。本轮未暂存、提交或推送。

### B1 最小能力边界（2026-11-07）

本轮依据正式题面六条规范确定 MVP 的最低能力范围，再次提取 PDF 第 21 页核对规范，保留现有解答源码。

| 能力项 | 最低要求 | 依据与验证 |
| --- | --- | --- |
| 输入范围 | 字符串长度为 0..1000；空串非法 | 正式规范；44 项定向检查及 16 组长度恰为 1000 的输入 |
| ASCII 语法 | 可选单个 + 或 -，随后至少一位 ASCII '0'..'9'；空白、额外符号和其他字节失败 | 定向语法检查及最大长度末尾字母、空格、空字符和 0x80 字节 |
| 前导零与零 | 允许任意长度的前导零，+0、-0 均得到 0 | 无符号、正号、负号的千字符零串；长补零后的正负端点 |
| 数值范围 | 包含 -2147483648 和 2147483647，正负越界一位均失败 | 千字符前导零配正负端点及对应越界值 |
| 溢出预防 | 每次乘加前判断是否仍在符号对应限值内，不执行危险运算后再检测 | 实现的 `(limit-digit)/10` 预检查；无符号及正负号长 9 串均拒绝 |
| 输出保护 | 仅全部成功后写 output；任何失败保留原值 | 每组分别以 0、9、int 最小值、int 最大值为初值，共 64 项检查 |
| 输入与调用 | 文本不变，每次调用独立，连续成功或失败互不污染局部解析状态 | 所有长度组合比较原文本副本；MVP 连续调用测试 |
| 实现限制与资源 | 不使用禁止的库转换、字符串流或自定义 class；O(n) 时间、O(1) 空间 | 实现只用字符下标与固定数量局部变量，写回前检查完整结果 |

最低本地验收标准为公开自检及检查器各通过 2/2、44 项定向检查通过、16 组千字符输入在四种 output 初值下的 64 项检查通过，且修改解答限于实现区。当前已满足。独立随机对照留待完成 B1 时补充，正式评分尚未核验。

新增 [b1_boundary_test.cpp](b1_boundary_test.cpp)。16 组输入均断言 `std::string::size()==1000`，包括三个零串、正负范围端点与前导零组合、正负越界一位、三个长溢出串及四种末尾非法字节。长度按 C++ string 字节数核对，解析仅接受 ASCII。

关键预期由构造确定：990 个零后接 2147483647 合法；正号后加 989 个零与该端点合法；负号后加 989 个零与 2147483648 得最小负数；对应越界一位的字符串均失败。999 个零后接非法字节也必须失败并保持 output，不能提交已经读到的零前缀。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/b1_boundary_test.cpp -o local_tests/build/b1_boundary_test.exe
.\local_tests\build\b1_boundary_test.exe
```

输出 `B1 boundary tests passed (16 strings, 1000 bytes each, 64 output checks)`，编译无警告，编译和运行退出码均为 0。本轮未修改解答，已核对源码哈希与此前通过的 B1 MVP 检查器报告一致，未重复运行无变化的公开测试。

前轮 MVP 尚未提交，本轮在原有工作区追加边界测试与记录，没有新提交。可按实际产出将 MVP 和边界一起整理为一次有明确范围的提交，Summary 同时说明实现与最大长度验证；本轮未暂存、提交或推送。

### B1 完成与本地验收（2026-11-07）

用户要求完成 B1。本轮保留现有解答，新增 [b1_validation.py](b1_validation.py)。参考方法使用 ASCII 字节正则 `[+-]?[0-9]+` 完整匹配，再用 Python 任意精度整数转换并核对明确的 32 位有符号范围。它与 C++ 逐位限幅累计分开实现，非 ASCII、空白和内嵌空字符不会被参考方法当作合法数字。

固定随机种子为 2627，共 1000 组输入。八类各 125 组，包括合法值、端点附近、补零值、越界值、格式变异、任意字节串、语法端点和随机数字串。全部输入长度不超过 1000，包含 12 组恰为 1000 字节的输入。实际有 331 组可接受、402 组格式非法、267 组数值超界。

每组分别以随机选择的初值、int 最小值、int 最大值以及跨批次连续复用的输出变量调用，共 4000 次 C++ 调用。其中连续调用 1000 次，从初值 9 开始，仅成功时更新参考状态；失败必须保留前一状态。共 2676 次失败输出保护检查全部通过，所有返回值与输出均和参考一致，每次调用后输入文本保持不变。输入经十六进制传输并按字节重建，覆盖空文本、换行、空字符和任意高位字节。

本轮重新编译并运行原文件、44 项定向检查、16 组千字符组合的 64 项输出检查，全部通过。三个常驻程序及临时随机驱动均以 C++17 和 `-Wall -Wextra -pedantic -Werror` 编译，无警告，编译与运行退出码均为 0。

实际执行：

```powershell
g++ -std=c++17 -Wall -Wextra -pedantic -Werror src/main/A1_b1.cpp -o local_tests/build/b1_public.exe
.\local_tests\build\b1_public.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/b1_mvp_test.cpp -o local_tests/build/b1_mvp_test.exe
.\local_tests\build\b1_mvp_test.exe
g++ -std=c++17 -Wall -Wextra -pedantic -Werror local_tests/b1_boundary_test.cpp -o local_tests/build/b1_boundary_test.exe
.\local_tests\build\b1_boundary_test.exe
python -X utf8 -B local_tests/b1_validation.py
python -X utf8 tools/check.py . --only b1 --output scores/b1-final
python -X utf8 tools/check.py . --output scores/assessment-with-b1-final --require-core
```

输出包括 `PUBLIC 2/2`、`B1 MVP tests passed (44 checks)`、`B1 boundary tests passed (16 strings, 1000 bytes each, 64 output checks)`、`B1 validation passed: 1000 random cases, 4000 calls, 1000 stateful calls (12 maximum-length cases, seed 2627)`。B1 专项可见组 2/2，公开选做分 10/20。

合并检查输出 `.: auto=60.0/60 bonus=10.0/20`，`--require-core` 退出码为 0；Q1–Q8 各 2/2，B1 2/2，共 18/18 个已实现任务的可见组通过。B2 尚未实现、0/2，不影响仅要求必做题的退出码，B1 的通过另由专项与合并报告确认。人工分待评，远程 CI 和正式评分尚未核验。

专项报告位于忽略目录 `scores/b1-final/`，合并报告位于 `scores/assessment-with-b1-final/`。已核对随机、专项、合并报告中的 B1 源码哈希一致，合并报告十个源码哈希均与当前文件一致。未发现需要修复的功能缺陷，解答源码保持不变。本轮未暂存、提交或推送。

## 5. 边界测试与缺陷记录

Q1 已有 25 项定向检查和 5350 组穷举，其中包含下表中的补充边界。当前尚无实际发现并修复的代码缺陷；后续遇到真实缺陷时记录，不为凑数量编造经历。

| 测试编号 | 题号与边界 | 输入 | 预期结果 | 实际结果 | 命令或测试文件 |
| --- | --- | --- | --- | --- | --- |
| T01 | Q1 负血量 | `ratio(-5,100)` | `0` | `0`，通过 | `q1_mvp_test.cpp` |
| T02 | Q1 血量超过上限 | `ratio(200,100)` | `100` | `100`，通过 | `q1_mvp_test.cpp` |
| T03 | Q1 最大血量无效 | `ratio(10,0)`、`ratio(10,-100)` | 均为 `-1` | 均为 `-1`，通过 | `q1_mvp_test.cpp` |
| T04 | Q1 大整数与截断 | `ratio(999999999999LL,1000000000000LL)` | `99` | `99`，通过 | `q1_mvp_test.cpp` |
| T05 | Q1 电量分档端点 | `report(7,2,3,b)`，`b` 依次为 19、20、59、60 | 状态依次 LOW、WARNING、WARNING、OK，完整报告格式匹配 | 四个完整字符串均与预期一致 | `q1_mvp_test.cpp` |
| T06 | Q1 无效血量仍处理电量 | `report(0,4,0,-7)` | `ID=0;HP=INVALID;BAT=0;STATE=LOW` | 与预期一致 | `q1_mvp_test.cpp` |
| T07 | Q1 电量 int 极值 | `report(9999,4,-1,INT_MAX)`、`report(0,-5,100,INT_MIN)` | 分别为 `ID=9999;HP=INVALID;BAT=100;STATE=OK`、`ID=0;HP=0;BAT=0;STATE=LOW` | 两个完整字符串均与预期一致 | `q1_mvp_test.cpp`，使用 `numeric_limits<int>` |
| T08 | Q1 极端血量 | `ratio(-10^12,1)`、`ratio(10^12,1)`、`ratio(10^12,-10^12)`（测试中使用整数字面量） | 依次为 0、100、-1 | 均与预期一致 | `q1_mvp_test.cpp` |
| T09 | Q1 输入不变 | `id=7,hp=-5,maxHp=100,battery=-7`，调用 report | 返回 `ID=7;HP=0;BAT=0;STATE=LOW`，四个输入变量保持原值 | 返回值和输入变量检查均通过 | `q1_mvp_test.cpp` |
| T10 | Q1 调用独立 | 多次无效和有效调用后再次 `report(7,2,3,20)` | `ID=7;HP=66;BAT=20;STATE=WARNING` | 与预期一致 | `q1_mvp_test.cpp` |
| T11 | Q1 百分比穷举 | 最大血量 1..100，每组血量为 -1..最大血量+1，共 5350 组 | 百分比在 0..100，满足精确向下取整不等式 | 全部通过 | `q1_mvp_test.cpp` |
| Q2-T01 | 完整标签匹配 | `edit_labels("cam2,cam",{{"cam","imu"}})` | `"cam2,imu"` | `"cam2,imu"` | `q2_mvp_test.cpp` |
| Q2-T02 | 删除末尾标签 | `edit_labels("a,b,c",{{"c",""}})` | `"a,b"` | `"a,b"` | `q2_mvp_test.cpp` |
| Q2-T03 | 清空后追加 | `edit_labels("a",{{"a",""},{"","b"}})` | `"b"` | `"b"` | `q2_mvp_test.cpp` |
| Q2-T04 | 变长后连续编辑 | `edit_labels("a,b,c",{{"a","camera"},{"b",""},{"c","imu"}})` | `"camera,imu"` | `"camera,imu"` | `q2_mvp_test.cpp` |
| Q2-T05 | 最大初始长度及 200 次追加 | 1000 字符名单，追加 200 个 32 字符标签 | 完整文本与列表参考一致，长 7600 | 与预期一致 | `q2_validation.py` |
| Q2-T06 | 清空后空操作 | 1000 字符名单，31 次删除、169 次空操作 | 空字符串 | 空字符串 | `q2_validation.py` |
| Q2-T07 | 末尾变长后恢复 | 1000 字符名单，末尾标签变长、恢复共 200 次 | 与初始文本一致 | 完全一致 | `q2_validation.py` |
| Q2-T08 | 随机序列独立对照 | 固定种子 2627，1000 组序列，每组至多 200 次编辑 | 与 Python 标签列表参考逐字一致 | 全部一致 | `q2_validation.py` |
| Q3-T01 | 阈值相等 | `alarms({2,2},2,4)` | 空序列 | 空序列 | `q3_mvp_test.cpp` |
| Q3-T02 | 负数窗口 | `alarms({-4,-3,-2},2,-6)` | `{2}` | `{2}` | `q3_mvp_test.cpp` |
| Q3-T03 | 大整数总和 | 三个 `10^9`，k=3，阈值 `2500000000LL` | `{2}` | `{2}` | `q3_mvp_test.cpp` |
| Q3-T04 | 最大正负窗口和 | n=k=200000，元素全为正或负 10^9，测试相等阈值及比总和小 1 的阈值 | 相等时空序列，严格大于时 `{199999}` | 四组均符合预期 | `q3_boundary_test.cpp` |
| Q3-T05 | 最大输出 | 200000 个 10^9，k=1，阈值 0 | 下标 0..199999 | 200000 项逐项一致 | `q3_boundary_test.cpp` |
| Q3-T06 | 大量重叠窗口 | 200000 个 10^9，k=100000，阈值 10^14-1 | 下标 99999..199999 | 100001 项逐项一致 | `q3_boundary_test.cpp` |
| Q3-T07 | 正负抵消 | 200000 个正负 10^9 交替，k=100000，阈值分别为 0 和 -1 | 分别为空序列与下标 99999..199999 | 两组均符合预期 | `q3_boundary_test.cpp` |
| Q3-T08 | 独立随机对照 | 固定种子 2627，1000 组长度不超过 100 的输入，覆盖合法和无效 k、相等阈值及大整数 | 与 Python 逐窗口重算结果逐项一致 | 全部一致 | `q3_validation.py` |
| Q4-T01 | 非法 RESET 不改值 | `execute({"SET 5","RESET x"})` | `{5,1,1}` | `{5,1,1}` | `q4_mvp_test.cpp` |
| Q4-T02 | 参数合法但结果越界 | `execute({"SET 1000000","ADD 1"})` | `{1000000,1,1}` | `{1000000,1,1}` | `q4_mvp_test.cpp` |
| Q4-T03 | 尾随字段拒绝后继续执行 | `execute({"SET 10","ADD 3 junk","ADD -4"})` | `{6,2,1}` | `{6,2,1}` | `q4_mvp_test.cpp` |
| Q4-T04 | 最大行数全成功或全失败 | 10000 行 ADD 1；10000 行空串 | 分别为 `{10000,10000,0}`、`{0,0,10000}` | 两组均符合预期 | `q4_boundary_test.cpp` |
| Q4-T05 | 上下限反复越界 | 各 2500 轮 SET 边界值、ADD 越界、RESET、ADD 另一边界值 | 最终值分别为 -1000000、1000000，accepted=7500、rejected=2500 | 两组均符合预期 | `q4_boundary_test.cpp` |
| Q4-T06 | 非法 RESET 保留状态 | SET 5 后 9999 次 RESET x | `{5,1,9999}` | `{5,1,9999}` | `q4_boundary_test.cpp` |
| Q4-T07 | 超长整数解析溢出 | 首行 SET 后跟 10000 个 9，后续 9999 行 ADD 1 | `{9999,9999,1}` | `{9999,9999,1}` | `q4_boundary_test.cpp` |
| Q4-T08 | 超长合法前导零 | SET + 后跟 10000 个 0 和 1，随后两行非法命令、9997 行 ADD 0 | `{1,9998,2}` | `{1,9998,2}` | `q4_boundary_test.cpp` |
| Q4-T09 | 独立随机对照 | 固定种子 2627，1000 组序列，每组至多 100 行，混合合法、非法命令及边界值 | value、accepted、rejected 与独立正则模型逐项一致 | 全部一致 | `q4_validation.py` |
| Q5-T01 | 单格边界 | `risk({"."})` | `{{0}}` | `{{0}}` | `q5_mvp_test.cpp` |
| Q5-T02 | 对角障碍不计 | `risk({"#.",".."})` | `{{-1,1},{1,0}}` | `{{-1,1},{1,0}}` | `q5_mvp_test.cpp` |
| Q5-T03 | 最后一个字符非法 | `risk({"..",".x"})` | 抛出 std::invalid_argument | 抛出相同异常 | `q5_mvp_test.cpp` |
| Q5-T04 | 最大全空或全障碍地图 | 300×300 的全点或全井号地图 | 全 0 或全 -1 的同尺寸矩阵 | 两组全部格子符合预期 | `q5_boundary_test.cpp` |
| Q5-T05 | 最大棋盘格地图 | 300×300 点、井号交替地图 | 障碍 -1，空地为其有效邻格数，角落 2、边缘 3、内部 4 | 逐格符合预期 | `q5_boundary_test.cpp` |
| Q5-T06 | 最长单行与单列 | 300 格，下标 149 处为障碍 | 该格 -1，相邻两格 1，其余 0 | 两组完整矩阵符合预期 | `q5_boundary_test.cpp` |
| Q5-T07 | 最大地图末尾非法 | 最后一格为 x，或最后一行少一格 | std::invalid_argument | 两组均抛出相同异常 | `q5_boundary_test.cpp` |
| Q5-T08 | 独立随机对照 | 固定种子 2627，750 组合法地图、250 组非法地图，尺寸不超过 20×20 | 合法地图完整矩阵与障碍累加模型一致，非法地图抛出指定异常 | 全部符合预期 | `q5_validation.py` |
| Q6-T01 | 血量优先于距离 | `{{7,3,4,1,true},{2,0,0,2,true}}`，range=5 | 返回 7 | 返回 7 | `q6_mvp_test.cpp` |
| Q6-T02 | 平局编号与零射程 | `{{9,0,0,3,true},{1,0,0,3,true}}`，range=0 | 返回 1 | 返回 1 | `q6_mvp_test.cpp` |
| Q6-T03 | 大整数距离求和 | `{{83,1000000,1000000,1,true}}`，range=1000000 | 返回 -1 | 返回 -1 | `q6_mvp_test.cpp` |
| Q6-T04 | 输入不变和调用独立 | 三目标列表选择后逐字段比较原副本；逆序选择；随后空输入及新候选 | 原内容不变、逆序仍选 70，后两次分别为 -1、123 | 全部符合预期 | `q6_mvp_test.cpp` |
| Q6-T05 | 最大规模全淘汰 | 100000 个目标，分别构造全不可见、全无血量、全在百万射程外 | 三组均返回 -1 | 均为 -1，输入不变 | `q6_boundary_test.cpp` |
| Q6-T06 | 最大规模末尾更新 | 100000 个目标，末尾目标分别血量最低或距离最近 | 两组均返回 99999 | 均为 99999，输入不变 | `q6_boundary_test.cpp` |
| Q6-T07 | 最大规模平局 | 100000 个同血量同距离目标，id 降序和升序 | 两组均返回 0 | 均为 0，输入不变 | `q6_boundary_test.cpp` |
| Q6-T08 | 最大规模仅末尾合格 | 100000 个目标，前 99999 个混合淘汰，末尾在 (-600000,-800000)，range=10^6 | 返回 99999 | 返回 99999，输入不变 | `q6_boundary_test.cpp` |
| Q6-T09 | 独立随机对照与重排 | 固定种子 2627，1000 组输入各按原序、逆序及随机重排调用 | 3000 次结果与筛选排序参考一致，每次输入不变 | 全部一致，628 组有候选、372 组无候选 | `q6_validation.py` |
| Q7-T01 | 空请求不冷却 | `simulate(4,80,10,30,{})` | `{0,0,4,80}` | `{0,0,4,80}` | `q7_mvp_test.cpp` |
| Q7-T02 | 先冷却再判断 | `simulate(1,100,10,10,{1})` | `{1,0,0,100}` | `{1,0,0,100}` | `q7_mvp_test.cpp` |
| Q7-T03 | 拒绝保留冷却 | `simulate(1,100,10,11,{1})` | `{0,1,1,90}` | `{0,1,1,90}` | `q7_mvp_test.cpp` |
| Q7-T04 | 无弹仍冷却 | `simulate(0,50,10,20,{1})` | `{0,1,0,40}` | `{0,1,0,40}` | `q7_mvp_test.cpp` |
| Q7-T05 | 零射击热量 | `simulate(1,100,0,0,{1})` | `{1,0,0,100}` | `{1,0,0,100}` | `q7_mvp_test.cpp` |
| Q7-T06 | 最大帧数全拒绝 | 10000 个请求 1，分别构造无弹和无冷却持续过热 | `{0,10000,0,0}`、`{0,10000,100,100}` | 两组四字段均一致 | `q7_boundary_test.cpp` |
| Q7-T07 | 周期恢复与末帧 | 10000 个请求 1，ammo=100、heat=100、cool=1、shot_heat=100 | 每 100 帧成功一次，返回 `{100,9900,0,100}` | 四字段均一致 | `q7_boundary_test.cpp` |
| Q7-T08 | 耗尽后继续冷却 | 10000 个请求 1，ammo=100、heat=100、cool=shot_heat=100 | `{100,9900,0,0}` | 四字段均一致 | `q7_boundary_test.cpp` |
| Q7-T09 | 仅末帧请求 | 前 9999 个请求为 0，最后为 1，ammo=1、heat=100、cool=1、shot_heat=100 | `{1,0,0,100}` | 四字段均一致 | `q7_boundary_test.cpp` |
| Q7-T10 | 独立随机对照与分段衔接 | 固定种子 2627，1000 组输入，各运行整段、前段和接续后段 | 3000 次四字段与事件参考一致，1000 次分段合并等于整段结果，输入不变 | 全部通过，包含 10 组万帧序列 | `q7_validation.py` |
| Q8-T01 | 非法记录不占编号 | `{{1,-1001},{1,30}}` | `{1,0,1,30,{1}}` | 全字段一致 | `q8_mvp_test.cpp` |
| Q8-T02 | 先验证再判重复 | `{{1,20},{1,1001}}` | `{1,0,1,20,{1}}` | 全字段一致 | `q8_mvp_test.cpp` |
| Q8-T03 | 乱序编号与血量夹取 | `{{9999,50},{2,100},{0,-1000},{1,10}}` | `{4,0,0,160,{0,1,2,9999}}` | 全字段一致 | `q8_mvp_test.cpp` |
| Q8-T04 | 极值索引保护 | id 分别为 int 最小值和最大值，hp=30 | 各计一次 invalid，ids 为空 | 均符合预期，无越界 | `q8_mvp_test.cpp` |
| Q8-T05 | 首次合法负血量保留 | `{{1,-5},{1,100}}` | `{1,1,0,0,{1}}` | 全字段一致 | `q8_mvp_test.cpp` |
| Q8-T06 | 最大规模全非法与大量重复 | 20000 条极值非法记录；20000 条相同合法记录 | 前者 invalid=20000；后者 valid=1、duplicate=19999、total_hp=100 | 全字段一致 | `q8_boundary_test.cpp` |
| Q8-T07 | 完整编号域与最大总量 | 反序 10000 个编号首次 hp=1000，再补 10000 条合法负血量重复 | valid=10000、duplicate=10000、total_hp=1000000，ids=0..9999 | 全字段与完整清单一致 | `q8_boundary_test.cpp` |
| Q8-T08 | 全编号验证顺序 | 分别构造 10000 条非法后合法、10000 条合法后非法 | 两组均 valid=10000、duplicate=0、invalid=10000 | 全字段与完整清单一致 | `q8_boundary_test.cpp` |
| Q8-T09 | 三类混合与守恒 | 5000 个编号各含非法、首次合法、合法重复、非法编号四条记录 | valid=5000、duplicate=5000、invalid=10000、total_hp=500000 | 全字段一致，输入不变 | `q8_boundary_test.cpp` |
| Q8-T10 | 独立参考与批次变换 | 固定种子 2627，1000 组输入，各运行原序、逆序、整批重复和空批次 | 4000 次统计与完整清单和稳定分组参考一致，重复公式及空批次重置成立 | 全部通过，包含 10 组两万条批次；361 组逆序总量变化均符合首次合法规则 | `q8_validation.py` |
| B1-T01 | 正负范围端点 | `"2147483647"`、`"-2147483648"`，初始 output=9 | 均成功，输出对应边界值 | 返回值与输出均一致 | `b1_mvp_test.cpp` |
| B1-T02 | 越界一位且保留输出 | `"2147483648"`、`"-2147483649"`，初始 output=9 | 均失败，output=9 | 均符合预期 | `b1_mvp_test.cpp` |
| B1-T03 | 最长输入 | 1000 个 '0'；1000 个 '9' | 前者成功得 0，后者失败且保留输出 | 均符合预期 | `b1_mvp_test.cpp` |
| B1-T04 | 字符串长度与 ASCII 检查 | 三字节文本 `12` 后接空字符；全角数字及 U+0661 的字节串 | 均失败且保留输出 | 均符合预期 | `b1_mvp_test.cpp` |
| B1-T05 | 最长补零端点 | 1000 字节的无符号、正号最大正数及负号最小负数组合 | 均成功写入对应端点，与原 output 无关 | 四种初值下均一致 | `b1_boundary_test.cpp` |
| B1-T06 | 最长补零越界 | 1000 字节的无符号及正号 2147483648、负号 2147483649 | 均失败，原 output 保持 | 四种初值下均一致 | `b1_boundary_test.cpp` |
| B1-T07 | 最后字节非法 | 1000 字节中末尾为 x、空格、空字符或 0x80，其余为符号和零 | 均失败，原 output 保持，文本不变 | 四种初值下均一致 | `b1_boundary_test.cpp` |
| B1-T08 | 独立随机参考与输出连续复用 | 固定种子 2627，1000 组字节串，各测试随机初值、int 两端及连续输出状态 | 4000 次返回值与输出匹配参考，失败保留原值，输入不变 | 全部通过，含 12 组千字节串、2676 次失败输出保护检查 | `b1_validation.py` |

实际缺陷记录格式：发现日期、现象、最小复现、原因、修改位置、修复方式、复测结果。当前暂无条目。

## 6. AI 使用与归档状态

- 已使用工具：Codex 桌面应用；用户使用 VS Code 编辑本地项目。
- 当前辅助范围：按用户要求实现 Q1–Q8 与 B1，核对正式规范、定向、规模或最大长度边界及独立参考结果，完成九个已实现任务的合并公开检查。
- 代码来源：Q1 的 `ratio`、`report`，Q2 的 `edit_labels`，Q3 的 `alarms`，Q4 的 `execute`，Q5 的 `risk`，Q6 的 `select_target`，Q7 的 `simulate`，Q8 的 `summarize`，B1 的 `parse_i32` 及对应本地测试由 Codex 生成并运行验证，用户尚未确认已逐段核对。
- 结果核对：通过 VS Code 项目记录、本地 Git 信息和实际文件读取交叉确认路径与状态；文档变更使用 Git 差异核对。
- 建议采纳情况：助手曾建议从 Q1 开始；用户随后明确选择 Q1，并要求先写 MVP。当前暂无已明确拒绝的代码建议。
- 归档核验（2026-11-07 Q6 边界任务）：已安装 Agent Session Commit 0.1.5 和 pre-commit 4.7.0，配置本仓库 Custom 来源及官方 hooks；模板配置文件未改。提交前链路已测试。用户的 `d995ef8` 已包含首个 bundle，读取和导出哈希核验均通过。
- 来源与范围：`export_agent_sessions.py` 选择本作业聊天 ID 或准确的仓库 cwd，仅导出用户和助手可见文字，保留原始时间、行号、cwd 与校验哈希。当前聊天原始 cwd 为 `D:\cpp`，因此未使用会跳过该聊天的原生 Codex 目录筛选。原始文件保留在本机；系统与开发者上下文、内部推理、工具载荷、工作区上下文和非文字附件不在导出范围内。
- 补充记录：Q1–Q5 开发时工具尚未配置，现存真实记录已在 `d995ef8` 补充导入，旧提交保持原样。不能据此声称早期提交当时已附归档，教师对覆盖范围的认可仍待确认。
- 本 Markdown 是人工整理的工作记录，不替代题目要求的原始会话归档。

完整配置、每次提交的检查方法与新 clone 安装步骤见 [提交与版本控制指南](git-workflow.md)。正在进行中的会话可能尚未完整写入本地来源，后续提交时继续刷新并核对覆盖范围。

## 7. 已完成工作与产出

| 日期 | 实际完成的工作 | 产出或证据 | 状态与限制 |
| --- | --- | --- | --- |
| 2026-11-06 | 阅读公共模板的 README 和 Markdown 题面 | 当前聊天中的要求概览 | 未开始实现，正式 PDF 逐页核对未完成 |
| 2026-11-07 | 定位 VS Code 中的个人作业克隆 | 本节所列本地路径、远程地址及 HEAD | 本地仓库信息已核实，未查询远程 CI |
| 2026-11-07 | 检查 Q1–Q8、B1、B2 实现区 | 十题均为模板 TODO | 未编译、未测试 |
| 2026-11-07 | 建立方向与产出记录，并添加 README 入口 | 本文件及 README 个人说明区 | 本地文档变更，尚未提交或推送 |
| 2026-11-07 | 记录用户的新方向和当前优先级 | 后续从 Q1 MVP 开始，当前先完成建档 | 仅记录计划，未修改 Q1 |
| 2026-11-07 | 按用户重新发起的任务实现 Q1 MVP | `src/main/A1_q1.cpp`、`local_tests/q1_mvp_test.cpp`，并更新 README 与本记录 | 公开自检、本地 17 项检查及检查器 Q1 2/2 通过；未提交 |
| 2026-11-07 | 按已验证的路线完成 Q1 本地验收 | 正式 Q1 规范核对，扩展测试与完成记录，`scores/q1-final/` 本地报告 | 25 项定向检查、5350 组穷举和 Q1 公开测试通过；未提交 |
| 2026-11-07 | 按用户的五条写作要求精简 README 个人说明 | 本节写作规则及 README 末尾两节 | 保留实现细节、测试结果和 AI 使用记录；源码未改 |
| 2026-11-07 | 自检 Q1 README 并补足具体信息 | 明确无效最大血量、夹取范围、分档结果和穷举范围，直接列出三个补充测试 | 对照实际代码和通过的测试核验；模板原文与源码未改 |
| 2026-11-07 | 实现 Q2 MVP，核对正式题面并完成本地自测 | `src/main/A1_q2.cpp`、`local_tests/q2_mvp_test.cpp`、README 和本记录 | 公开自检、25 项本地检查及检查器 Q2 2/2 通过；未提交 |
| 2026-11-07 | 完成 Q2 扩展验证并更新 README | `local_tests/q2_validation.py`、README、本记录及本地 `scores/q2-final/` 报告 | 3 组规模边界、1000 组随机对照及检查器 Q2 2/2 通过；归档待配置 |
| 2026-11-07 | 最后确认 Q1、Q2 当前版本可以编译运行 | 四个 C++ 程序重新编译执行，重跑随机对照和 Q1、Q2 检查器 | 全部退出码为 0，已核对报告与源码哈希；源码未改 |
| 2026-11-07 | 记录中文 Summary 要求，并建立版本历史观察基线 | 第 3 节协作规则及第 8 节提交与文件对应表 | 核对本地历史、分支、远程地址和跟踪引用；本轮只改文档 |
| 2026-11-07 | 实现 Q3 滑动窗口 MVP，补充测试和 README | `src/main/A1_q3.cpp`、`local_tests/q3_mvp_test.cpp`、README、本记录 | 公开自检、20 项本地检查及检查器 Q3 2/2 通过；未提交 |
| 2026-11-07 | 确定 Q3 最小能力边界，补测最大输入规模 | `local_tests/q3_boundary_test.cpp`、README、本记录 | 8 组 n=200000 测试通过；解答源码未改 |
| 2026-11-07 | 完成 Q3，补齐独立随机对照并重新实跑 | `local_tests/q3_validation.py`、README、本记录及 `scores/q3-final/` 本地报告 | 公开测试 2/2、20 项定向检查、8 组最大规模和 1000 组随机对照全部通过；源码未改 |
| 2026-11-07 | 实现 Q4 MVP，补充命令解析测试与 README | `src/main/A1_q4.cpp`、`local_tests/q4_mvp_test.cpp`、README、本记录 | 公开自检、25 组本地命令序列及检查器 Q4 2/2 通过；未提交 |
| 2026-11-07 | 确定 Q4 最小能力边界，补测最大行数与长数字 | `local_tests/q4_boundary_test.cpp`、README、本记录 | 正式 PDF 复核完成，8 组各 10000 行测试通过，源码未改 |
| 2026-11-07 | 完成 Q4，补齐独立随机对照并重新实跑 | `local_tests/q4_validation.py`、README、本记录及 `scores/q4-final/` 本地报告 | 公开测试 2/2、25 组定向、8 组规模及 1000 组随机对照均通过；源码未改 |
| 2026-11-07 | 实现 Q5 MVP，核对正式题面并补充测试 | `src/main/A1_q5.cpp`、`local_tests/q5_mvp_test.cpp`、README、本记录 | 公开自检、20 项本地检查及检查器 Q5 2/2 通过；未提交 |
| 2026-11-07 | 确立 Q5 最小能力边界，补测最大地图 | `local_tests/q5_boundary_test.cpp`、README、本记录 | 8 组规模与格式边界通过，解答源码未改 |
| 2026-11-07 | 完成 Q5，补齐合法与非法地图的独立随机对照 | `local_tests/q5_validation.py`、README、本记录及 `scores/q5-final/` 本地报告 | 公开测试 2/2、20 项定向、8 组规模与 1000 组随机对照通过；源码未改 |
| 2026-11-07 | 优化提交位置与版本控制，配置会话来源和仓库代理 | `git-workflow.md`、导出脚本及其测试、README、本记录；本地 Git 配置及 hooks | 5 项测试与真实提交前链路通过；完整检查 Q1–Q5 通过，Q6–Q8 未实现；未提交或推送 |
| 2026-11-07 | 实现 Q6 目标选择 MVP，核对正式规范并补测 | `src/main/A1_q6.cpp`、`local_tests/q6_mvp_test.cpp`、README、本记录 | 公开自检和检查器各 2/2、30 项本地检查通过；未提交或推送 |
| 2026-11-07 | 确定 Q6 最小功能边界，补测最大规模并核对新提交 | `local_tests/q6_boundary_test.cpp`、README、本记录及首包校验 | 8 组各 100000 目标全部通过；解答未改；本轮未提交或推送 |
| 2026-11-07 | 完成 Q6，补齐独立随机对照和输入重排验证 | `local_tests/q6_validation.py`、README、本记录及 `scores/q6-final/` 本地报告 | 公开组 2/2、30 项定向、8 组规模及 1000 组输入的 3000 次调用均通过；解答未改 |
| 2026-11-07 | 实现 Q7 热量与弹仓仿真 MVP，核对正式规范并补测 | `src/main/A1_q7.cpp`、`local_tests/q7_mvp_test.cpp`、README、本记录 | 公开自检和检查器各 2/2、30 项定向检查通过；未提交或推送 |
| 2026-11-07 | 确认 Q7 最低功能边界，补测最大帧数并核对新提交 | `local_tests/q7_boundary_test.cpp`、README、本记录 | 8 组各 10000 帧全部通过；解答未改；本轮未提交或推送 |
| 2026-11-07 | 完成 Q7，补齐独立随机参考与分段衔接验证 | `local_tests/q7_validation.py`、README、本记录及 `scores/q7-final/` 本地报告 | 可见组 2/2、30 项定向、8 组规模、3000 次对照与 1000 项衔接检查均通过；解答未改 |
| 2026-11-07 | 实现 Q8 遥测汇总 MVP，核对正式规范并补测 | `src/main/A1_q8.cpp`、`local_tests/q8_mvp_test.cpp`、README、本记录 | 公开自检和检查器各 2/2、32 项定向检查通过；未提交或推送 |
| 2026-11-07 | 确认 Q8 最小能力边界，补测最大记录数和完整编号域 | `local_tests/q8_boundary_test.cpp`、README、本记录 | 8 组各 20000 条记录全部通过，完整 ids 与最大总量核验；解答未改；本轮未提交或推送 |
| 2026-11-07 | 完成 Q8 随机对照及所有必做题整体验收 | `local_tests/q8_validation.py`、README、本记录、更新后的提交指南及本地报告 | Q8 4000 次对照通过；Q1–Q8 可见组 16/16，公开自动分 60/60；保留已有注释删除差异 |
| 2026-11-07 | 实现 B1 十进制解析 MVP，核对正式规范并补测 | `src/main/A1_b1.cpp`、`local_tests/b1_mvp_test.cpp`、README、本记录及提交指南说明 | 公开自检与检查器各 2/2、44 项定向检查通过；未提交或推送 |
| 2026-11-07 | 确定 B1 最小能力边界，补测千字符组合与输出初值 | `local_tests/b1_boundary_test.cpp`、README、本记录 | 16 组最大长度输入、64 项输出检查通过；解答未改；MVP 与本轮产出均未提交 |
| 2026-11-07 | 完成 B1 随机对照与连续输出保护验证，更新合并验收 | `local_tests/b1_validation.py`、README、本记录、提交指南及本地报告 | B1 4000 次对照通过；Q1–Q8 与 B1 可见组 18/18，自动分 60/60、选做分 10/20；解答未改 |

## 8. Git 增量记录

| 提交或工作区阶段 | 内容 | 验证 | Git 状态 |
| --- | --- | --- | --- |
| `a80983b91bf8195fad769163f0828b29ab7f4b61` | 克隆中已有的初始模板提交 | 本地读取提交信息 | 已存在于当前本地历史 |
| 本次建档 | 新增协作记录，README 增加入口 | 文档内容、链接和修改范围检查 | 未提交，待用户审阅 |
| Q1 MVP | 实现 `ratio`、`report`，补充本地测试并记录结果 | GCC 编译、公开自检、17 项本地检查及检查器 Q1 可见组通过；实现区外内容未变 | 未提交，未推送 |
| Q1 完成 | 保留已验证的算法，补充正式规范对照、定向与穷举测试，更新文档 | 两次编译均启用 `-Werror`；公开自检、25 项定向检查、5350 组穷举、检查器 Q1 2/2 通过 | 未提交，未推送 |
| Q2 MVP | 实现标签顺序编辑，新增边界测试与说明 | 公开自检、25 项本地检查、检查器 Q2 2/2 通过，编译无警告 | 未提交，未推送 |
| Q2 完成验证 | 新增独立列表参考模型、规模边界及随机对照，补全 README | 3 组规模边界、1000 组随机对照、Q2 可见组 2/2 通过 | 新脚本与文档未提交 |
| Q3 MVP | 实现滑动窗口，新增边界测试，补充 README 和过程记录 | 公开自检、20 项本地检查、检查器 Q3 2/2 通过 | 未提交，未推送 |
| Q3 最小能力边界 | 明确完整题面范围和验收下限，新增最大规模测试 | 8 组 n=200000 边界通过，覆盖最大输出和大窗口 | 本轮测试与文档未提交 |
| Q3 完成 | 新增独立随机参考验证，重编译并运行全部 Q3 检查，更新完成状态 | 可见组 2/2、20 项定向、8 组规模、1000 组随机对照均通过 | 本轮脚本与文档未提交 |
| Q4 MVP | 实现命令完整验证后提交状态，补充测试与说明 | 公开自检、25 组本地命令序列及 Q4 可见组 2/2 通过 | 未提交，未推送 |
| Q4 最小能力边界 | 明确命令、数值、失败、计数及资源范围，补测 10000 行与超长数字 | 8 组最大行数测试通过，正式 PDF 已复核 | 本轮测试与文档未提交 |
| Q4 完成 | 新增独立正则参考验证，重新实跑全部 Q4 程序并更新完成记录 | 可见组 2/2、25 组定向、8 组规模及 1000 组随机对照均通过 | 本轮脚本与文档未提交 |
| Q5 MVP | 实现完整验证地图后计算四邻域风险，补充基础测试和说明 | 公开自检、20 项本地检查及 Q5 可见组 2/2 通过 | 未提交，未推送 |
| Q5 最小能力边界 | 明确地图、格式、计算和资源范围，补充最大地图与末尾非法输入 | 8 组边界通过，最大合法矩阵逐格核验 | 本轮测试与文档未提交 |
| Q5 完成 | 新增障碍累加参考模型，重新实跑全部 Q5 检查并更新完成记录 | 可见组 2/2、20 项定向、8 组规模与 1000 组随机对照均通过 | 本轮脚本与文档未提交 |
| Q6 MVP | 实现一次遍历筛选和三级比较，新增定向测试与 README 说明 | 公开自检 2/2、30 项本地检查、检查器 Q6 可见组 2/2 通过 | 本轮解答、测试和文档未提交；前轮版本控制优化亦未提交 |
| Q6 最小功能边界 | 明确完整契约与验收下限，新增 10 万目标测试，核验首次归档 | 8 组规模测试通过，输入保持不变，首包哈希一致 | 解答已在 `d995ef8`；本轮测试和文档未提交 |
| Q6 完成 | 新增排序参考与 1000 组随机输入，重跑全部 Q6 检查并更新完成记录 | 可见组 2/2、30 项定向、8 组规模、3000 次对照调用均通过 | 本轮随机验证与文档未提交 |
| Q7 MVP | 实现逐帧冷却与请求处理，新增顺序、资源计数和边界测试 | 公开自检 2/2、30 项定向检查、检查器 Q7 可见组 2/2 通过 | 本轮解答、测试和文档未提交 |
| Q7 最低功能边界 | 明确完整契约和最低验收要求，新增 10000 帧规模测试 | 8 组规模测试、守恒关系与输入不变检查均通过 | 解答已在 `3effe9e`；本轮测试和文档未提交 |
| Q7 完成 | 新增事件参考与分段衔接验证，重跑全部 Q7 检查并更新完成记录 | 可见组 2/2、30 项定向、8 组规模、1000 组随机输入的 3000 次调用均通过 | 本轮随机验证与文档未提交 |
| Q8 MVP | 实现验证、分类、首次合法累计和编号整理，新增极值与守恒测试 | 公开自检 2/2、32 项定向检查、检查器 Q8 可见组 2/2 通过 | 本轮解答、测试和文档未提交 |
| Q8 最小能力边界 | 明确完整契约和最低验收要求，新增 20000 条记录与全编号域测试 | 8 组规模、完整清单、最大总量及守恒检查均通过 | 解答已在 `3545076`；本轮测试和文档未提交 |
| Q8 完成 | 新增稳定分组参考和批次变换测试，重跑 Q8 并执行完整必做题检查 | Q8 4000 次对照及 Q1–Q8 可见组 16/16 均通过 | 本轮脚本与文档未提交；工作区另有八个源文件的注释删除差异 |
| B1 MVP | 实现 ASCII 十进制逐字符解析、溢出预防与失败输出保护，新增定向测试 | 公开自检 2/2、44 项定向检查、检查器 B1 可见组 2/2 通过 | 本轮解答、测试和文档未提交 |
| B1 最小能力边界 | 明确完整契约和最低验收要求，新增 16 组最大长度输入与四种输出初值检查 | 64 项输出检查和文本不变检查通过 | 前轮解答与本轮测试均未提交，无新历史节点 |
| B1 完成 | 新增严格语法与任意精度整数参考，重跑 B1 并更新合并检查 | 44 项定向、64 项边界输出、4000 次随机调用和已实现任务的可见组均通过 | 本轮脚本与文档未提交 |

以上阶段的“未提交”是当时的状态。最后运行自检记录现已包含在 `2913986` 中。下面按实际文件变更建立历史基线，后续继续记录新增节点。

后续按题目或实际缺陷记录增量。提交后记录真实最终 SHA；若归档 hook 改写了提交，以改写后的 SHA 为准。助手本轮未执行 Git 提交或推送。

### 工作历史观察基线（2026-11-07）

用户说明稍后会询问提交位置与版本控制问题。本节先保存检查时的事实，之后根据实际历史分析。

- 当前仓库路径与远程地址见第 2 节，当前分支为 `main`，跟踪 `origin/main`。
- 本轮开始时工作区和暂存区均无改动。
- 本地 HEAD 与本地保存的 `origin/main` 都是 `2913986feead0c2e01e339a27073dd2185e45075`。本次未联网刷新远程引用，这一结果只反映本地记录。
- 以下时间均取自 Git 提交记录，时区为 `+08:00`。

| 提交 | 时间 | 原 Summary | 实际涉及的文件与内容 |
| --- | --- | --- | --- |
| `7b96887` | 2026-11-07 12:24:23 | Q1 draft | Q1 解答、Q1 本地测试、README、协作记录 |
| `02f7ef7` | 2026-11-07 12:29:03 | README写的像人类语言一点 | README、协作记录 |
| `8d92775` | 2026-11-07 12:39:31 | mvp检查通过，确定后续路线 | Q2 解答、Q2 MVP 测试、README、协作记录 |
| `b5866a7` | 2026-11-07 12:50:04 | 确认了一下边界 | Q2 扩展验证脚本、README、协作记录 |
| `2913986` | 2026-11-07 12:53:35 | q1 q2 再次测试，可以提交版本 | 仅修改协作记录，记录 Q1、Q2 最终实跑结果 |
| `221057b` | 2026-11-07 12:59:25 | 记录中文提交摘要要求和版本历史基线&#96; | 仅修改协作记录，增加中文 Summary 要求和历史观察基线 |
| `b79a897` | 2026-11-07 13:04:41 | 实现Q3滑动窗口MVP，补充边界测试和README说明 | Q3 解答、Q3 MVP 测试、README、协作记录 |
| `c3b838d` | 2026-11-07 13:09:13 | 明确Q3最小能力边界，补充最大规模测试 | Q3 最大规模测试、README、协作记录 |
| `5cef470` | 2026-11-07 13:14:47 | 补充Q3随机对照测试，更新验收结果 | Q3 独立随机验证脚本、README、协作记录 |
| `32ecdad` | 2026-11-07 13:20:38 | 实现Q4命令事务MVP，补充解析测试和README说明 | Q4 解答、Q4 MVP 测试、README、协作记录 |
| `c66f696` | 2026-11-07 13:26:15 | 明确Q4最小能力边界，补充最大行数和超长数字测试 | Q4 最大行数与长数字测试、README、协作记录 |
| `4c6dbea` | 2026-11-07 13:34:45 | 补充Q4随机对照测试，更新验收结果 | Q4 独立随机验证脚本、README、协作记录 |
| `4d879e4` | 2026-11-07 13:43:08 | 实现Q5风险图MVP，补充地图校验与边界测试 | Q5 解答、Q5 MVP 测试、README、协作记录 |
| `c3b0f3b` | 2026-11-07 13:47:52 | 明确Q5最小能力边界，补充最大地图测试 | Q5 最大地图测试、README、协作记录 |
| `f7b2626` | 2026-11-07 13:54:13 | 补充Q5随机对照测试，更新验收结果 | Q5 独立随机验证脚本、README、协作记录 |
| `d995ef8` | 2026-11-07 17:20:10 | 实现Q6目标选择MVP，补充定向测试和README说明 | Q6 解答与定向测试、README、协作记录；同时包含前轮三份版本控制文件和首个会话归档 |
| `f1d2553` | 2026-11-07 17:27:01 | 明确Q6最小功能边界，补充十万目标规模测试 | Q6 规模测试、README、协作记录、版本控制指南及新增会话归档 |
| `f2e4c3` | 2026-11-07 17:32:29 | 补充Q6随机对照和顺序不变性测试，完成本地验收 | Q6 随机验证脚本、README、协作记录及新增会话归档 |
| `3effe9e` | 2026-11-07 17:38:52 | 实现Q7热量与弹仓仿真MVP，补充定向测试和README说明 | Q7 解答与定向测试、README、协作记录及新增会话归档 |
| `2e77b39` | 2026-11-07 20:07:10 | 明确Q7最低功能边界，补充万帧规模与守恒测试 | Q7 规模测试、README、协作记录及新增会话归档 |
| `12b17d3` | 2026-11-07 20:13:27 | 补充Q7随机对照和分段衔接测试，完成本地验收 | Q7 随机验证脚本、README、协作记录及新增会话归档 |
| `3545076` | 2026-11-07 20:26:09 | 实现Q8遥测汇总MVP，补充分类去重和守恒测试 | Q8 解答与定向测试、README、协作记录及新增会话归档 |
| `e21f1b3` | 2026-11-07 20:35:18 | 明确Q8最小能力边界，补充两万记录和完整编号域测试 | Q8 规模测试、README、协作记录 |
| `4954375` | 2026-11-07 20:35:18 | 明确Q8最小能力边界，补充两万记录和完整编号域测试 | 仅新增会话归档，父提交为 `e21f1b3` |
| `b613c33` | 2026-11-07 20:52:38 | 补充Q8随机对照与批次验证，完成必做题本地验收 | Q8 随机验证、README、协作记录、提交指南、会话归档及八个必做题文件的一行注释删除 |
| `0581ff7` | 2026-11-07 22:40:10 | 实现B1解析并明确最小能力边界，补充千字符组合测试 | B1 解答、MVP 与边界测试、README、协作记录、提交指南及会话归档 |

这些提交均由本地历史读取，助手没有执行相应提交。历史表中的 `&#96;` 表示原提交摘要末尾的反引号。Q5 完成任务开始时，main 与本地保存的 origin/main 都在 `c3b0f3b`；版本控制优化任务开始时，Q5 完成产出已包含在 `f7b2626`，工作区干净。

### 版本控制优化与验证（2026-11-07）

实际结论是保留当前个人仓库和 `main`，继续按 MVP、边界、完成验收分阶段提交。16 个历史提交中有 15 个增量，达到模板参考线。改进重点为 Summary 与实际文件对应、同步更新当前进度表、补足会话记录。旧历史不重写。

终端 Git 直连 GitHub 超时。读取系统当前代理后，仅为本仓库配置 `http.https://github.com/.proxy=http://127.0.0.1:7897`，随后 `git ls-remote origin refs/heads/main` 成功，远端与本地均为 `f7b26261528d22bdc1375d885ef888460a0a7060`。依赖本机现有代理服务，切换网络时按指南调整。全局配置和 SSL 校验未改。

在忽略目录 `.venv-agent-session-commit/` 安装归档工具并设置本地 hooks。Windows 下最初使用 `/bin/sh` 的 legacy hook 被 Python 框架解析后无法启动，已改用当前虚拟环境的 Python 解释器。实跑 `.git/hooks/pre-commit` 通过，并断言前后 HEAD、暂存区二进制差异相同。未运行会改写提交的 post-commit，也未进行提交或推送。

新增导出脚本的 5 项自动检查通过，覆盖可见内容筛选、项目选择、错误远端拒绝、增量前缀保持及用户已有 hook 保护。来源状态能识别两份真实会话导出和一份清单；这些文件位于忽略目录，不等于已生成 bundle。原始会话不改写，新增文字记录在下一次正常提交导入。

复现命令：

```powershell
.\.venv-agent-session-commit\Scripts\python.exe -B -m unittest discover -s local_tests -p test_export_agent_sessions.py
.\.venv-agent-session-commit\Scripts\agent-session-commit.exe status
python -X utf8 tools/check.py . --output scores/version-control-audit --require-core
```

完整检查结果为 Q1–Q5 各 2/2 通过；Q6–Q8、B1/B2 均仍为模板未实现。自动分 31.2/60、选做分 0/20；`--require-core` 因必做题尚未完成而退出 1。报告位于忽略目录 `scores/version-control-audit/`，不是正式成绩或远程 CI 结果。本轮解答源码未改。

新版 [提交与版本控制指南](git-workflow.md) 记录提交位置、中文 Summary 示例、暂存与推送顺序、归档校验、新 clone 安装及正式交卷条件。后续工作中记录上一次已完成提交的最终 SHA，避免为记录当前提交自身 SHA 而反复产生文档提交。

### Q8 阶段版本观察（2026-11-07）

本轮读到两个标题和作者时间相同的相邻提交：`e21f1b3` 保存测试与文档，`4954375` 仅新增归档，后者直接以此前者为父提交。它们是当前历史中的两个节点，不是同一提交的两个可见版本。归档工具源码仍使用 amend；本次为何产生后续独立节点尚未定位，不推断由用户或某个客户端造成。现有历史保持原样。

本轮开始时 main 较保存的 origin/main 领先 1；随后读取到 origin/main 已在 `4954375`，与 HEAD 相同。助手未执行网络刷新、提交或推送，这些本地引用不证明最终 GitHub CI 状态。后续提交等待钩子结束，核对实际文件归属、bundle 与最终 SHA，再推送。

## 9. 下次继续时

1. 读取本记录，重新检查 Git 状态和最新源码。
2. Q1–Q8 与 B1 实现及本地验收已完成；按用户指引安排 B2、逐段理解或正式提交流程，不自动开始 B2。
3. 正常提交后检查最终 SHA 与新增 `.agent-sessions/bundles/`，持续核对真实归档覆盖范围，再推送；首包已在 `d995ef8` 核验。
4. 完成授权范围内的工作，记录实际改动、测试证据、产出与下一步。

Q1–Q8 与 B1 的实现和本地验收已验证，合并公开自动分 60/60、选做分 10/20，人工分待评。B2 尚未实现。GitHub CI、截止日期和正式提交状态尚未核验，本轮没有执行 Git 提交或推送。
