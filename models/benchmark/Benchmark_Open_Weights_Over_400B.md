| Category / Benchmark                 | Minimax-M3-428B | Nemotron 3 Ultra | GLM-5.2      | Inkling        | DeepSeek-V4-Pro (Preview) | DeepSeek-V4-Pro Max | Kimi K3      |
| ------------------------------------ | --------------- | ---------------- | ------------ | -------------- | ------------------------- | ------------------- | ------------ |
| **Weight Type**                      | Open weights    | Open weights     | Open weights | Open weights   | Open weights              | Open weights        | Open weights |
| **Model Info**                       |                 |                  |              |                |                           |                     |              |
| AA Index (v4.1)                      | –               | 38.0%            | 51.0%        | 41.0%          | 44.0%                     | –                   | –            |
| Params (B) (activated / total)       | 428             | 55 / 550         | 40 / 753     | 41 / 975       | 49 / 1600                 | 49 / 1600           | 50 / 2800    |
| **Agentic (coding)**                 |                 |                  |              |                |                           |                     |              |
| SWEBench Verified                    | –               | 70.7%            | –            | 77.6%          | –                         | 80.6%               | –            |
| SWEBench Pro (public)                | 59.0%           | 46.4%            | 62.1%        | 54.3%          | –                         | 55.4%               | –            |
| Terminal Bench 2.1 (best harness)    | 64.0%           | 56.4%            | 82.7%        | 63.8%          | 72.1%                     | 66.5%               | 88.3%        |
| Terminal-Bench 2.1 (Terminus-2)      | 64.0%           | –                | 81.0%        | –              | –                         | 64.0%               | –            |
| Terminal-Bench 2.1 (Claude Code)     | –               | –                | 82.7%        | –              | –                         | 66.5%               | –            |
| Terminal-Bench 2.0                   | –               | –                | –            | –              | –                         | –                   | –            |
| SciCode                              | –               | 39.9%            | –            | 46.1%          | –                         | –                   | –            |
| SWE-bench Multilingual               | –               | 67.7%            | –            | –              | –                         | 76.2%               | –            |
| DeepSWE                              | –               | –                | 46.2%        | –              | 12.8%                     | 9.0%\*              | 69%          |
| SWE Atlas (Codebase QnA)             | 37.9%           | –                | –            | –              | –                         | 27.2%               | –            |
| SWE Atlas - RF                       | –               | –                | –            | –              | –                         | –                   | –            |
| SWE Atlas - TW                       | 30.8%           | –                | –            | –              | –                         | –                   | –            |
| NL2Repo                              | 42.1%           | –                | 48.9%        | –              | 38.5%                     | –                   | –            |
| Claw-Eval Avg                        | –               | –                | –            | –              | –                         | 75.8%               | –            |
| Claw-Eval Pass^3                     | –               | –                | –            | –              | –                         | –                   | –            |
| QwenClawBench                        | –               | –                | –            | –              | –                         | –                   | –            |
| Cybergym                             | –               | –                | –            | –              | 52.7%                     | –                   | –            |
| DSBench-FullStack †                  | –               | –                | 61.8%        | –              | 41.8%                     | –                   | –            |
| DSBench-Hard †                       | –               | –                | 54.5%        | –              | 31.1%                     | –                   | –            |
| **Agentic (general)**                |                 |                  |              |                |                           |                     |              |
| GDPval-AA v2                         | –               | 1164             | –            | 1238           | –                         | –                   | –            |
| MCP Atlas (public / all)             | –               | 47.4/44.7%       | –            | 78.8/76.0%     | –                         | –                   | –            |
| Tau 3 Banking                        | –               | 13.8%            | –            | 23.7%          | –                         | –                   | –            |
| BrowseComp (with context management) | –               | 63.0%            | –            | 77.1%          | –                         | –                   | –            |
| Toolathlon Verified                  | –               | 34.3%\*          | 59.9%        | 45.5%\*        | 55.9%                     | 55.9%\*             | –            |
| AA-Briefcase                         | –               | 870              | –            | 839            | –                         | –                   | –            |
| Agents' Last Exam                    | –               | –                | 23.8%        | –              | 16.5%                     | –                   | –            |
| AutomationBench Public               | –               | –                | 12.9%        | –              | 12.8%                     | –                   | –            |
| DeepSearch QA                        | –               | –                | –            | –              | –                         | –                   | –            |
| WildClawBench                        | –               | –                | –            | –              | –                         | –                   | –            |
| Gaia2                                | –               | –                | –            | –              | –                         | –                   | –            |
| SkillsBench (with skills)            | –               | –                | –            | –              | –                         | –                   | –            |
| SkillsBench Avg5                     | –               | –                | –            | –              | –                         | –                   | –            |
| QwenWebBench                         | –               | –                | –            | –              | –                         | –                   | –            |
| OSWorld-Verified                     | –               | –                | –            | –              | –                         | –                   | –            |
| **Reasoning (general)**              |                 |                  |              |                |                           |                     |              |
| GPQA Diamond                         | –               | 86.7%            | –            | 87.2%          | –                         | –                   | –            |
| HLE (text only)                      | –               | 26.6%            | –            | 29.7%          | –                         | –                   | –            |
| HLE (with tools)                     | –               | 37.4%            | –            | 46.0%          | –                         | –                   | –            |
| LiveCodeBench v6                     | –               | –                | –            | –              | –                         | –                   | –            |
| AA-LCR                               | –               | –                | –            | –              | –                         | –                   | –            |
| Beam128K                             | –               | –                | –            | –              | –                         | –                   | –            |
| **Reasoning (abstract)**             |                 |                  |              |                |                           |                     |              |
| ARC-AGI-1                            | –               | –                | –            | 79.5%          | –                         | –                   | –            |
| ARC-AGI-2                            | –               | –                | –            | 36.5%          | –                         | –                   | –            |
| **Chat**                             |                 |                  |              |                |                           |                     |              |
| IFBench                              | –               | 81.4%            | –            | 79.8%          | –                         | –                   | –            |
| **Safety**                           |                 |                  |              |                |                           |                     |              |
| StrongREJECT                         | –               | 98.7%            | –            | 98.6%          | –                         | –                   | –            |
| FORTRESS (adversarial)               | –               | 77.6%            | –            | 78.0%          | –                         | –                   | –            |
| FORTRESS (benign)                    | –               | 90.6%            | –            | 95.9%          | –                         | –                   | –            |
| **Security and Privacy**             |                 |                  |              |                |                           |                     |              |
| CI Memories                          | –               | –                | –            | –              | –                         | –                   | –            |
| Siren AgentDojo                      | –               | –                | –            | –              | –                         | –                   | –            |
| **Vision**                           |                 |                  |              |                |                           |                     |              |
| MMMU Pro (Standard 10)               | –               | –                | –            | 73.5%          | –                         | –                   | –            |
| Charxiv RQ (original / with python)  | –               | –                | –            | 78.1/82.0%     | –                         | –                   | –            |
| ScreenSpot Pro                       | –               | –                | –            | –              | –                         | –                   | –            |
| OmniDocBench v1.5                    | –               | –                | –            | –              | –                         | –                   | –            |
| **Audio**                            |                 |                  |              |                |                           |                     |              |
| Audio MC                             | –               | –                | –            | 56.6%          | –                         | –                   | –            |
| MMAU                                 | –               | –                | –            | 77.2%          | –                         | –                   | –            |
| VoiceBench                           | –               | –                | –            | 91.4%          | –                         | –                   | –            |
