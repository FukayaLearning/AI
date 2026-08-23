| Category / Benchmark                 | Laguna S 2.1 | Minimax M2.7 | Inkling-Small | DeepSeek V4 Flash | Tencent Hy3  | MiMo V2.5    | Qwen 3.8 397B-A17B | Ornith 1.5-397B |
| ------------------------------------ | ------------ | ------------ | ------------- | ----------------- | ------------ | ------------ | ------------------ | --------------- |
| **Weight Type**                      | Open weights | Open weights | Open weights  | Open weights      | Open weights | Open weights | Open weights      | Open weights    |
| **Model Info**                       |              |              |               |                   |              |              |                   |                 |
| AA Index (v4.1)                      | –            | 38.0%        | 40.0%         | 50.0%             | –            | 37.0%        | 34.0%             | –               |
| Params (B) (activated / total)       | 8 / 118      | 10 / 230     | 12 / 276      | 13 / 284          | 21 / 295     | 15 / 310     | 17 / 397          | 397             |
| **Agentic (coding)**                 |              |              |               |                   |              |              |                   |                 |
| SWEBench Verified                    | –            | 79.9%        | 80.2%         | 79.0%             | –            | 71.0%        | 76.4%             | 82.4%           |
| SWEBench Pro (public)                | 59.4%        | 56.2%        | 55.9%         | 52.6%             | 57.9%        | 56.1%        | 51.6%             | 62.2%           |
| Terminal Bench 2.1 (best harness)    | 70.2%        | 55.4%        | 64.7%         | 82.7%             | 71.7%        | 63.7%        | 53.5%             | 78.2%           |
| Terminal-Bench 2.1 (Terminus-2)      | –            | –            | –             | –                 | –            | –            | 53.5%             | 77.5%           |
| Terminal-Bench 2.1 (Claude Code)     | –            | –            | –             | –                 | –            | –            | 48.6%             | 78.2%           |
| Terminal-Bench 2.0                   | –            | –            | –             | –                 | –            | –            | 52.5%             | –               |
| SciCode                              | –            | 47.0%        | 48.7%         | 44.9%             | –            | 43.1%        | 42.0%             | –               |
| SWE-bench Multilingual               | 78.5%        | –            | –             | –                 | 75.8%        | –            | 69.3%             | 78.9%           |
| DeepSWE                              | 40.4%        | –            | –             | 54.4%             | –            | –            | –                 | –               |
| SWE Atlas (Codebase QnA)             | 46.2%        | –            | –             | –                 | –            | –            | 20.4%             | 41.2%           |
| SWE Atlas - RF                       | –            | –            | –             | –                 | –            | –            | 18.4%             | 42.6%           |
| SWE Atlas - TW                       | –            | –            | –             | –                 | –            | –            | 18.5%             | 39.1%           |
| NL2Repo                              | –            | –            | –             | 54.2%             | –            | –            | 36.8%             | 48.2%           |
| Claw-Eval Avg                        | –            | –            | –             | –                 | –            | –            | 70.7%             | 77.1%           |
| Claw-Eval Pass^3                     | –            | –            | –             | –                 | –            | –            | 48.1%             | –               |
| QwenClawBench                        | –            | –            | –             | –                 | –            | –            | 51.8%             | –               |
| Cybergym                             | –            | –            | –             | 76.7%             | –            | –            | –                 | –               |
| DSBench-FullStack †                  | –            | –            | –             | 68.7%             | –            | –            | –                 | –               |
| DSBench-Hard †                       | –            | –            | –             | 59.6%             | –            | –            | –                 | –               |
| **Agentic (general)**                |              |              |               |                   |              |              |                   |                 |
| GDPval-AA v2                         | –            | 1159         | 1269          | 1189              | –            | 1145         | 962               | –               |
| MCP Atlas (public / all)             | –            | 49.4%/–      | 79.6/79.2%    | 69.0%/–           | –            | –            | 74.2%/–           | –               |
| Tau 3 Banking                        | –            | 8.9%         | 15.5%         | 22.9%             | –            | 6.6%         | 13.4%             | –               |
| BrowseComp (with context management) | –            | 76.3%        | 77.4%         | 73.2%             | –            | –            | 78.6%             | –               |
| Toolathlon Verified                  | 49.7%        | 47.5%        | 54.4%         | 70.3%             | –            | 49.1%        | 40.7%             | –               |
| AA-Briefcase                         | –            | –            | 917           | 833               | –            | –            | –                 | –               |
| Agents' Last Exam                    | –            | –            | –             | 25.2%             | –            | –            | –                 | –               |
| AutomationBench Public               | –            | –            | –             | 25.1%             | –            | –            | –                 | –               |
| DeepSearch QA                        | –            | –            | –             | –                 | –            | –            | –                 | –               |
| WildClawBench                        | –            | –            | –             | –                 | –            | –            | –                 | –               |
| Gaia2                                | –            | –            | –             | –                 | –            | –            | –                 | –               |
| SkillsBench (with skills)            | –            | –            | –             | –                 | –            | –            | –                 | –               |
| SkillsBench Avg5                     | –            | –            | –             | –                 | –            | –            | 30.0%             | –               |
| QwenWebBench                         | –            | –            | –             | –                 | –            | –            | 1186              | –               |
| OSWorld-Verified                     | –            | –            | –             | –                 | –            | –            | –                 | –               |
| **Reasoning (general)**              |              |              |               |                   |              |              |                   |                 |
| GPQA Diamond                         | –            | 87.4%        | 89.5%         | 89.4%             | –            | 84.9%        | 88.4%             | –               |
| HLE (text only)                      | –            | 28.1%        | 31.6%         | 32.1%             | –            | 25.2%        | 28.7%             | –               |
| HLE (with tools)                     | –            | 40.3%        | 47.8%         | 45.1%             | –            | 40.0%        | 48.3%             | –               |
| LiveCodeBench v6                     | –            | –            | –             | –                 | –            | –            | 83.6%             | –               |
| AA-LCR                               | –            | –            | –             | –                 | –            | –            | –                 | –               |
| Beam128K                             | –            | –            | –             | –                 | –            | –            | –                 | –               |
| **Reasoning (abstract)**             |              |              |               |                   |              |              |                   |                 |
| ARC-AGI-1                            | –            | –            | 84.0%         | –                 | –            | –            | –                 | –               |
| ARC-AGI-2                            | –            | –            | 40.1%         | –                 | –            | –            | –                 | –               |
| **Chat**                             |              |              |               |                   |              |              |                   |                 |
| IFBench                              | –            | 75.7%        | 82.2%         | 79.2%             | –            | 67.1%        | 78.8%             | –               |
| **Safety**                           |              |              |               |                   |              |              |                   |                 |
| StrongREJECT                         | –            | 99.4%        | 98.4%         | 97.4%             | –            | 99.3%        | 99.4%             | –               |
| FORTRESS (adversarial)               | –            | 86.3%        | 71.6%         | 32.0%             | –            | 64.8%        | 77.3%             | –               |
| FORTRESS (benign)                    | –            | 90.1%        | 96.9%         | 99.2%             | –            | 94.6%        | 95.4%             | –               |
| **Security and Privacy**             |              |              |               |                   |              |              |                   |                 |
| CI Memories                          | –            | –            | –             | –                 | –            | –            | –                 | –               |
| Siren AgentDojo                      | –            | –            | –             | –                 | –            | –            | –                 | –               |
| **Vision**                           |              |              |               |                   |              |              |                   |                 |
| MMMU Pro (Standard 10)               | –            | –            | 74.0%         | –                 | –            | 75.4%        | 77.3%             | –               |
| Charxiv RQ (original / with python)  | –            | –            | 77.4/81.3%    | –                 | –            | 81.0%/–      | 80.8%/–           | –               |
| ScreenSpot Pro                       | –            | –            | –             | –                 | –            | –            | –                 | –               |
| OmniDocBench v1.5                    | –            | –            | –             | –                 | –            | –            | –                 | –               |
| **Audio**                            |              |              |               |                   |              |              |                   |                 |
| Audio MC                             | –            | –            | 54.9%         | –                 | –            | 30.4%        | –                 | –               |
| MMAU                                 | –            | –            | 77.0%         | –                 | –            | 73.6%        | –                 | –               |
| VoiceBench                           | –            | –            | 90.1%         | –                 | –            | 86.4%        | –                 | –               |
