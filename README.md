# 9路圍棋開局指南 (9x9 Go Openings Guide)

## 專案目標 (Project Goal)

本專案旨在收集、整理網路上公開的 9 路圍棋 (9x9 Go) 開局知識，並將其編寫成一本結構清晰、易於學習的開局指南。我們希望為圍棋愛好者提供一個快速上手 9 路棋的資源，理解小棋盤對弈中的效率、攻防與策略。

This project aims to collect and organize publicly available 9x9 Go opening knowledge from the internet into a well-structured and easy-to-learn guide. We hope to provide Go enthusiasts with a resource to quickly get started with the 9x9 board, understanding the concepts of efficiency, attack, and defense in small-board gameplay.

## 本書目錄 (Table of Contents)

*   **[前言 (Foreword)](./FOREWORD.md)**
    *   為什麼要學習 9 路圍棋？
    *   小棋盤的特性

*   **[第一章：基礎概念 (Chapter 1: Basic Concepts)](./CONCEPTS.md)**
    *   角、邊、中央的價值
    *   效率與棋形
    *   先手與後手

*   **第二章：開局分類 (Chapter 2: Opening Patterns)**
    *   **天元開局 (5-5, Tengen)**
        *   [詳見 `openings/5-5_tengen.md`](./openings/5-5_tengen.md)
    *   **星位開局 (4-4, Star Point)**
        *   [詳見 `openings/4-4_star_point.md`](./openings/4-4_star_point.md)
    *   **小目開局 (3-4, Komoku)**
        *   [詳見 `openings/3-4_komoku.md`](./openings/3-4_komoku.md)
    *   **三三開局 (3-3, San-san)**
        *   [詳見 `openings/3-3_san-san.md`](./openings/3-3_san-san.md)
    *   **其他開局 (Other Openings)**
        *   [詳見 `openings/others.md`](./openings/others.md)

*   **附錄 (Appendix)**
    *   術語表
    *   參考資料

## 檔案結構 (File Structure)

```
.
├── README.md         # 專案總覽與目錄 (Project overview and main ToC)
├── FOREWORD.md       # 前言
├── CONCEPTS.md       # 基礎概念
└───openings/         # 各類開局變化的詳細文件
    ├── 5-5_tengen.md
    ├── 4-4_star_point.md
    ├── 3-4_komoku.md
    ├── 3-3_san-san.md
    └───others.md
```

## 如何貢獻 (How to Contribute)

歡迎您一起參與，讓這本指南更完善！

1.  **Fork** 本專案。
2.  建立您的功能分支 (`git checkout -b feature/YourFeature`)。
3.  提交您的變更 (`git commit -m 'Add some feature'`)。
4.  將分支推送到遠端 (`git push origin feature/YourFeature`)。
5.  開啟一個 **Pull Request**。

您也可以開啟 **Issue** 來回報錯誤、或建議新增內容。

## 版權 (License)

本專案採用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 授權。歡迎在遵守授權條款的前提下自由分享與改作。
