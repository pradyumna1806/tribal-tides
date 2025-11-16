# Deployment Checklist for Render.com

## Pre-Deployment Steps

### 1. Build Frontend
```bash
cd frontend
npm install
npm run build
```
✅ This creates `backend/dist/` with the built Vue app

### 2. Verify Files
- ✅ `backend/dist/index.html` exists
- ✅ `backend/dist/assets/` contains CSS and JS files
- ✅ `backend/requirements.txt` includes `gunicorn`
- ✅ `render.yaml` is in project root
- ✅ `backend/app.py` serves static files from `dist/`

### 3. Test Locally (Optional)
```bash
cd backend
python app.py
# Visit http://localhost:5000 - should see Vue app
```

### 4. Commit to Git
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

## Render.com Deployment

### 5. Create Web Service
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `tribal-tides`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click "Create Web Service"

### 6. Initialize Database (After First Deployment)
Once deployed, you can:
- Use Render's Shell to run: `python seed_data.py`
- Or the database will auto-create on first API call (but will be empty)

### 7. Verify Deployment
- Visit your Render URL (e.g., `https://tribal-tides.onrender.com`)
- Check that:
  - ✅ Homepage loads
  - ✅ API endpoints work (`/api/products`)
  - ✅ Navigation works
  - ✅ No console errors

## Post-Deployment

### 8. Seed Database (if needed)
If you need to populate the database:
1. Go to Render Dashboard → Your Service → Shell
2. Run: `python seed_data.py`

### 9. Monitor Logs
- Check Render logs for any errors
- Monitor application performance

## Troubleshooting

### Frontend Not Loading
- Check that `backend/dist/` exists in your repository
- Verify build was successful
- Check Render logs for errors

### API Not Working
- Verify database exists: `backend/database.db`
- Check that tables are created (auto-created on startup)
- Run `seed_data.py` if database is empty

### 503 Error
- Frontend not built - run `npm run build` in frontend directory
- Ensure `backend/dist/` is committed to git

### Database Issues
- SQLite file is created in `backend/` directory
- Ensure write permissions on Render
- Database persists between deployments

## Updating After Deployment

1. Make code changes
2. Build frontend: `cd frontend && npm run build`
3. Commit: `git add . && git commit -m "Update" && git push`
4. Render auto-deploys on push

---

**Note**: The free tier on Render may spin down after inactivity. First request after spin-down may take longer.

