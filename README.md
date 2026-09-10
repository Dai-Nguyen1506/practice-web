# Thực hành thiết kế web

## Demo sản phẩm

**Bước 1: Clone Repository**

```powershell
git clone https://github.com/Dai-Nguyen1506/practice-web
cd practice
```

**Bước 2: Kích hoạt môi trường python**

```powershell
cd backend
python -m venv .venv
.venv/Scripts/avtivate
```

**Bước 3: Chạy dự án**

```powershell
pip install -r requirements.txt
uvicorn main:app --reload
```

**Bước 4: Demo**

Mở file `frontend/house_form.html`, kích hoạt Live Server, nhập số liệu và bấm nút `Predict` để kiểm tra kết quá