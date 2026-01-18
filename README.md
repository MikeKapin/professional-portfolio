# Mike Kapin - Professional Portfolio Website

## Overview

This is a professional portfolio website showcasing Mike Kapin's expertise as an HVAC educator, EdTech developer, and AI integration specialist. The site maintains clear separation between institutional employment (Fanshawe College) and independent ventures (LARK Labs).

## Site Structure

```
mike-kapin-portfolio/
├── index.html           # Homepage with overview and highlights
├── about.html           # Comprehensive background and philosophy
├── experience.html      # Professional experience and employment history
├── technical.html       # Technical skills (AI, software development, MCP servers)
├── lark-labs.html       # LARK Labs independent venture (clearly separated)
├── contact.html         # Contact information with proper email separation
├── styles.css           # Complete styling for all pages
└── README.md           # This file
```

## Key Features

### ✅ Clear Institutional/Independent Separation
- **Fanshawe College**: Listed factually as employment history
- **LARK Labs**: Clearly marked as independent venture with disclaimers
- Proper email separation (personal vs. institutional)
- Independence statements on every page

### ✅ Comprehensive Content
- 20+ years HVAC industry experience
- 10+ years teaching experience
- AI integration and software development expertise
- 6 production MCP servers
- LARK Labs platform with 3 AI-powered learning tools

### ✅ Professional Design
- Modern, responsive layout
- Clean color scheme (blue/orange/dark)
- Mobile-friendly navigation
- Card-based layouts for content sections
- Consistent branding throughout

### ✅ Legal Protection
- Disclaimers on every page
- Clear IP ownership statements
- Proper attribution and separation
- Professional contact boundaries

## Pages Breakdown

### 1. Homepage (index.html)
- Hero section with tagline
- Core competencies grid
- Career highlights timeline
- Quick navigation to other sections

### 2. About (about.html)
- Professional background narrative
- Educational philosophy ("Technology should serve people, not the other way around")
- Journey through HVAC → Education → Technology
- Unique value proposition
- Education & credentials
- Professional development certifications

### 3. Experience (experience.html)
- Current position at Fanshawe College (factual, professional)
- 20+ years industry experience (HVAC business ownership)
- Training & safety experience
- Key achievements grid

### 4. Technical Skills (technical.html)
- Software development (Python, JavaScript, TypeScript, Node.js)
- AI integration (Claude API, MCP servers, prompt engineering)
- Frameworks (Next.js, React, Vercel)
- Educational technology expertise
- Document processing & generation
- Media & content creation
- HVAC technical expertise

### 5. LARK Labs (lark-labs.html)
- **CRITICAL**: Clear independence statements at top
- Mission & vision
- Technical architecture (6 MCP servers)
- AI-powered learning tools:
  - Code Compass
  - HVAC Jack
  - Gas Tech Tutor
- Automated content generation systems
- IP ownership disclaimers

### 6. Contact (contact.html)
- **Two separate email addresses:**
  - mike@mikekapin.ca (personal/LARK Labs/consulting)
  - m_kapin@fanshawec.ca (Fanshawe institutional only)
- LARK Labs website link
- Areas of interest
- Collaboration opportunities
- Professional boundaries statement

## Color Scheme

```css
Primary Blue: #2563eb
Secondary Dark: #0f172a
Accent Orange: #f59e0b
Text Color: #1e293b
Light Background: #f8fafc
Gray: #64748b
Success Green: #10b981
```

## Fonts

```css
System font stack for performance:
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif
```

## Responsive Design

- **Desktop**: Full navigation, multi-column grids
- **Tablet**: Adapted layouts, maintained readability
- **Mobile**: Single column, stacked navigation, touch-friendly

Breakpoint: 768px

## Next Steps for Claude Code

### Immediate Enhancements:

1. **Add Favicon**
   - Create/add Mike Kapin favicon
   - Add to all HTML files

2. **Optimize Images** (when added)
   - Profile photo
   - LARK Labs logo
   - Project screenshots
   - Compress and optimize

3. **Mobile Menu**
   - Add hamburger menu for mobile
   - JavaScript for toggle functionality
   - Smooth animations

4. **Smooth Scrolling**
   - Add smooth scroll behavior
   - Anchor links for long pages

5. **Contact Form** (optional)
   - Add functional contact form
   - Form validation
   - Email integration

6. **Analytics** (optional)
   - Google Analytics
   - Privacy-compliant tracking

7. **SEO Optimization**
   - Meta descriptions
   - Open Graph tags
   - Twitter cards
   - Structured data

### Optional Enhancements:

8. **Dark Mode Toggle**
   - CSS variables for themes
   - LocalStorage preference saving
   - Smooth transitions

9. **Animation Effects**
   - Fade-in on scroll
   - Hover effects enhancement
   - Page transitions

10. **Portfolio Section**
    - Add specific project showcases
    - Screenshots and demos
    - Case studies

11. **Blog Section** (future)
    - Educational content
    - Technical tutorials
    - Industry insights

12. **Testimonials Section**
    - Student feedback
    - Colleague endorsements
    - Industry recognition

## Domain Setup

**Recommended domain**: mikekapin.ca

### Steps:
1. Purchase domain from Canadian registrar
2. Point DNS to hosting provider
3. Set up email forwarding (mike@mikekapin.ca → personal email)
4. Add SSL certificate (HTTPS)

### Hosting Options:
- **Vercel** (Recommended): Free, easy deployment, great performance
- **Netlify**: Similar to Vercel, good free tier
- **GitHub Pages**: Free, simple, static hosting
- **Traditional Hosting**: Hostinger, HostPapa, etc.

## Deployment Guide

### Option 1: Vercel (Recommended)

```bash
# Install Vercel CLI
npm install -g vercel

# Initialize in project directory
cd mike-kapin-portfolio
vercel

# Follow prompts for deployment
```

### Option 2: GitHub Pages

```bash
# Create repository
git init
git add .
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/yourusername/portfolio.git
git push -u origin main

# Enable GitHub Pages in repository settings
# Select 'main' branch
```

### Option 3: Netlify

1. Drag and drop folder into Netlify dashboard
2. Or connect GitHub repository
3. Automatic deployment on push

## File Structure for Deployment

```
portfolio/
├── index.html
├── about.html
├── experience.html
├── technical.html
├── lark-labs.html
├── contact.html
├── styles.css
├── favicon.ico (add this)
├── images/ (add this)
│   ├── profile.jpg
│   ├── lark-labs-logo.png
│   └── projects/
└── README.md
```

## Important Notes

### ⚠️ Legal Protection

1. **LARK Labs Independence**: Every mention includes disclaimer
2. **Email Separation**: Two distinct contact methods
3. **IP Ownership**: Clear statements about personal projects
4. **Institutional Facts**: Fanshawe listed factually, professionally

### ⚠️ COI Compliance

The site maintains clear separation:
- ✅ Fanshawe experience = factual employment history
- ✅ LARK Labs = independent venture with disclaimers
- ✅ Personal technical skills = professional development
- ✅ Contact info = separate emails for different purposes

### ⚠️ Professional Boundaries

- All disclaimers present on every page
- Footer disclaimer on all pages
- Clear independence statements
- Proper attribution and ownership

## Testing Checklist

Before going live:

- [ ] All links work (internal and external)
- [ ] Responsive design tested (mobile, tablet, desktop)
- [ ] All images load correctly
- [ ] Contact emails correct
- [ ] LARK Labs link works (https://www.larklabs.org)
- [ ] All disclaimers present
- [ ] Grammar and spelling checked
- [ ] Browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Load time acceptable
- [ ] SSL certificate active (HTTPS)

## Maintenance

### Regular Updates:
- Update experience as roles change
- Add new projects/skills
- Update certifications
- Refresh content annually

### Monitor:
- Broken links
- Contact form submissions (if added)
- Analytics data (if added)
- Site performance

## Support Resources

- HTML/CSS Reference: [MDN Web Docs](https://developer.mozilla.org)
- Vercel Deployment: [Vercel Docs](https://vercel.com/docs)
- GitHub Pages: [GitHub Docs](https://docs.github.com/pages)
- Responsive Design: [CSS Tricks](https://css-tricks.com)

## Version History

- **v1.0** (January 2026): Initial site creation
  - 6 complete pages
  - Responsive design
  - Legal compliance
  - Ready for deployment

## Contact for Site Development

For questions about this website code:
- **Email**: mike@mikekapin.ca
- **LARK Labs**: www.larklabs.org

---

**Built with:** HTML5, CSS3, Responsive Design
**Philosophy:** "Technology should serve people, not the other way around"
**Status:** Ready for Claude Code enhancement and deployment

## Quick Start

```bash
# View the site locally
# Option 1: Python
python -m http.server 8000

# Option 2: Node.js
npx http-server

# Open browser to:
http://localhost:8000
```

Then hand off to Claude Code for enhancements! 🚀
