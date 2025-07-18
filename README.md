了解Django ViewSet概念
===

### 
使用 **Poetry + Django + Django REST Framework (DRF)** 快速建立一個支援 CRUD 操作的 API 專案

### 基本功能
- 初始化開始：
    - `poetry new` → `startproject` → `startapp`
- 建立 Model、Serializer、ViewSet
- 用 `DefaultRouter` 建立自動 URL
- CRUD API 路徑整理（含圖）
- 遷移與啟動測試流程

### 進階功能
- 使用者資料過濾 (`get_queryset`)
- 自動附加 user (`perform_create`)
- 自訂端點 `/share/`
- 權限控制：登入才能讀寫、Admin 才能刪改