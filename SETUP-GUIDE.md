# Professional Portfolio - Setup Guide

## Current Status

Your portfolio has been transformed with the LARK Labs dark theme and is ready for personalization!

### What's Complete:
- LARK Labs dark theme (glassmorphism, gradients, animations)
- Responsive design for all devices
- Social media links (LinkedIn, YouTube) in footer
- Photo placeholders on About, LARK Labs, and Experience pages
- 6 complete pages: Home, About, Experience, Technical Skills, LARK Labs, Contact
- Modern CSS with 1,094 lines of styling

---

## NEXT STEPS: What You Need to Do

### 1. Add Your Photos (REQUIRED)

Save your three photos with these exact filenames:

**Photo 1: Professional Headshot**
- Save as: `images/profile/headshot.jpg`
- Your first photo (portrait in office)
- Used on: About page, Contact page
- Recommended: Crop to square (800x800px)

**Photo 2: LARK Labs Conference**
- Save as: `images/lark-labs/conference-presentation.jpg`
- Your second photo (speaking at LARK Labs booth)
- Used on: LARK Labs page
- Keep original ratio (landscape)

**Photo 3: Teaching at Fanshawe**
- Save as: `images/teaching/fanshawe-classroom.jpg`
- Your third photo (teaching in classroom)
- Used on: Experience page
- Keep original ratio (landscape)

**Image Optimization:**
- Compress images to < 500KB each for fast loading
- Use tools like: TinyJPG.com or Squoosh.app
- Keep quality at 80-85%

---

### 2. Update Your LinkedIn URL (REQUIRED)

Open each HTML file and replace the LinkedIn placeholder.

**Files to update:** All 6 HTML files

**Find:** `https://www.linkedin.com/in/YOUR_LINKEDIN_USERNAME/`

**Replace with:** Your actual LinkedIn URL

Example: `https://www.linkedin.com/in/mike-kapin/`

---

### 3. Test Your Portfolio Locally

**Start local server:**
```bash
cd "C:/LocalProjects/Professional Portfolio"
python3 -m http.server 8000
```

Then open: http://localhost:8000

**Check:**
- All photos display correctly
- Social links work (open in new tabs)
- Dark theme looks good
- Responsive design works
- All navigation links work

---

## GITHUB DEPLOYMENT

### Step 1: Initialize Git

```bash
cd "C:/LocalProjects/Professional Portfolio"
git init
git add .
git commit -m "Initial portfolio with LARK Labs dark theme"
```

### Step 2: Create GitHub Repository

1. Go to github.com
2. Click "New Repository"
3. Name it: `portfolio` or `yourusername.github.io`
4. Do NOT initialize with README
5. Copy the repository URL

### Step 3: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to repository Settings
2. Click "Pages"
3. Source: Deploy from branch
4. Branch: main, folder: / (root)
5. Save

Live at: `https://YOUR_USERNAME.github.io/REPO_NAME/`

---

## FILE STRUCTURE

```
Professional Portfolio/
├── index.html
├── about.html
├── experience.html
├── technical.html
├── lark-labs.html
├── contact.html
├── styles.css (1,094 lines)
├── SETUP-GUIDE.md (this file)
├── images/
│   ├── profile/headshot.jpg
│   ├── lark-labs/conference-presentation.jpg
│   └── teaching/fanshawe-classroom.jpg
```

---

## COLOR SCHEME

LARK Labs colors:
- Primary Blue: #3498db
- Charcoal: #2c3e50
- Success Green: #27ae60
- Warning Orange: #f39c12
- Pure Black: #1a1a1a

---

## QUICK CHECKLIST

Before going live:

- [ ] All 3 photos added
- [ ] Photos compressed (< 500KB)
- [ ] LinkedIn URL updated in all files
- [ ] All pages tested locally
- [ ] Navigation works
- [ ] Social links work
- [ ] Responsive design tested
- [ ] Git repository created
- [ ] Pushed to GitHub
- [ ] GitHub Pages enabled

---

Built with LARK Labs design principles
