# Professional Portfolio - Netlify Deployment Guide

## 🚀 Your Portfolio is Ready!

All updates complete and ready for deployment:
- ✅ Professional content and styling
- ✅ LARK Labs page with conference presentation photo
- ✅ Code Compass correctly described (Gas Code Search Tool)
- ✅ All images properly organized
- ✅ Responsive design
- ✅ Contact information updated

---

## 📋 Pre-Deployment Checklist

Before deploying, verify:
- ✅ All HTML files present (index, about, experience, technical, lark-labs, contact)
- ✅ All images loading correctly
- ✅ Contact information accurate
- ✅ Links working properly
- ✅ No placeholder text remaining

---

## 🌐 Domain Options

### Option 1: Free Netlify Subdomain
**Cost**: FREE
**Domain**: `your-site-name.netlify.app`
- Instant setup, no purchase needed
- Professional enough for portfolio
- Can upgrade to custom domain later
- Example: `mike-kapin-portfolio.netlify.app`

### Option 2: Custom Domain (.com, .dev, .io)
**Recommended Domain Registrars**:

**Namecheap** (Most Popular)
- .com: ~$13/year
- .dev: ~$15/year
- .io: ~$35/year
- Website: https://www.namecheap.com

**Google Domains / Squarespace Domains**
- .com: ~$12/year
- .dev: ~$12/year
- Website: https://domains.google.com (now Squarespace)

**Cloudflare Registrar** (At-cost pricing, no markup)
- .com: ~$9-10/year
- .dev: ~$10/year
- Website: https://www.cloudflare.com/products/registrar/

**GoDaddy** (Beware of renewal prices)
- .com: ~$12/year (first year, higher renewal)
- Website: https://www.godaddy.com

### Suggested Domain Names for Your Portfolio:
- `mikekapin.com` ⭐ (Professional, simple)
- `mikekapin.dev` (Developer-focused)
- `kapin.io` (Tech-focused, shorter)
- `mikekapin.ca` (Canadian focus)
- `larklabs.com` (If focusing on LARK Labs branding)

---

## 🚀 Netlify Deployment Methods

### Method 1: Drag & Drop (Easiest - 2 minutes)

1. **Visit Netlify**
   - Go to: https://app.netlify.com
   - Sign up / Log in (GitHub/GitLab/Email)

2. **Deploy**
   - Click "Add new site" → "Deploy manually"
   - Drag the entire `Professional Portfolio` folder into the upload area
   - Wait ~30 seconds for deployment

3. **Your Site is Live!**
   - You'll get a URL like: `random-name-123456.netlify.app`
   - Click "Site settings" to customize the subdomain

4. **Change Subdomain Name** (Optional)
   - Site settings → "Change site name"
   - Enter: `mike-kapin-portfolio` (or your choice)
   - New URL: `mike-kapin-portfolio.netlify.app`

### Method 2: GitHub + Netlify (Best for Updates)

1. **Create GitHub Repository**
   ```bash
   cd "C:\Users\m_kap\Desktop\Professional Portfolio"
   git init
   git add .
   git commit -m "Initial portfolio deployment"
   gh repo create portfolio --public --source=. --push
   ```

2. **Connect to Netlify**
   - Go to: https://app.netlify.com
   - "Add new site" → "Import an existing project"
   - Choose "GitHub"
   - Select your `portfolio` repository
   - Deploy settings:
     - Build command: (leave empty)
     - Publish directory: `/`
   - Click "Deploy site"

3. **Automatic Updates**
   - Any time you push to GitHub, Netlify auto-deploys
   - No need to manually upload files again

### Method 3: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Navigate to portfolio
cd "C:\Users\m_kap\Desktop\Professional Portfolio"

# Login
netlify login

# Deploy
netlify deploy --prod
```

---

## 🔗 Adding a Custom Domain to Netlify

### Step 1: Purchase Domain
1. Choose a registrar (Namecheap, Cloudflare, etc.)
2. Search for your desired domain name
3. Purchase (usually ~$10-15/year for .com)
4. Complete registration

### Step 2: Connect Domain to Netlify

**In Netlify Dashboard:**
1. Go to your site → "Domain settings"
2. Click "Add custom domain"
3. Enter your domain: `mikekapin.com`
4. Click "Verify" → "Add domain"

**In Your Domain Registrar (e.g., Namecheap):**
1. Log into your domain registrar
2. Find "DNS Settings" or "Nameservers"
3. Choose one option:

**Option A: Netlify DNS (Recommended - Easiest)**
- In Netlify: Get your nameservers (e.g., `dns1.p01.nsone.net`)
- In Registrar: Replace nameservers with Netlify's
- Wait 24-48 hours for DNS propagation

**Option B: Custom DNS Records**
- Add A record: `@` → `75.2.60.5` (Netlify's load balancer)
- Add CNAME: `www` → `your-site.netlify.app`
- Wait ~1 hour for DNS propagation

### Step 3: Enable HTTPS (Automatic)
- Netlify automatically provides free SSL certificates
- HTTPS enabled within minutes of domain connection
- Your site: `https://mikekapin.com` ✅

---

## 📊 Recommended Domain for Your Portfolio

Based on your profile:

**Primary Recommendation**: `mikekapin.com`
- ✅ Professional and simple
- ✅ Your full name
- ✅ Easy to remember and share
- ✅ Great for personal branding
- ✅ Cost: ~$10-13/year

**Alternative**: `mikekapin.dev`
- ✅ Shows developer focus
- ✅ Modern and tech-focused
- ✅ Cost: ~$12-15/year

**If LARK Labs focused**: `larklabs.com` or `larklabs.org`
- ✅ Company branding
- ✅ Professional for business
- ✅ Can host both portfolio + LARK Labs content

---

## 🎯 Step-by-Step: Complete Deployment

### Quick Start (15 minutes total)

**Step 1: Deploy to Netlify (5 minutes)**
```
1. Go to https://app.netlify.com
2. Sign up with GitHub or Email
3. "Add new site" → "Deploy manually"
4. Drag "Professional Portfolio" folder
5. Wait for deployment
```

**Step 2: Test Your Site (2 minutes)**
```
1. Open the Netlify URL
2. Test all pages (Home, About, Experience, Technical, LARK Labs, Contact)
3. Verify images load
4. Check mobile responsiveness
```

**Step 3: Purchase Domain (5 minutes)**
```
1. Go to Namecheap or Cloudflare
2. Search: "mikekapin.com"
3. Add to cart and checkout
4. Complete domain registration
```

**Step 4: Connect Domain (3 minutes)**
```
1. In Netlify: Site settings → Add custom domain
2. Copy Netlify nameservers
3. In Namecheap: Paste nameservers
4. Wait 1-24 hours for DNS propagation
```

---

## 💰 Total Cost Breakdown

### Option 1: Free Netlify Subdomain
- **Cost**: $0/year
- **Domain**: `mike-kapin-portfolio.netlify.app`
- **Perfect for**: Getting started immediately

### Option 2: Custom .com Domain
- **Domain**: ~$13/year (Namecheap)
- **Hosting**: $0/year (Netlify free tier)
- **SSL**: $0/year (automatic)
- **Total**: ~$13/year
- **Perfect for**: Professional portfolio

### Option 3: Premium .dev Domain
- **Domain**: ~$15/year
- **Hosting**: $0/year (Netlify)
- **SSL**: $0/year (automatic)
- **Total**: ~$15/year
- **Perfect for**: Developer-focused branding

---

## 🔥 What to Do Right Now

### Immediate Next Steps:

**1. Deploy to Netlify (Do this first - FREE)**
```
→ Go to https://app.netlify.com
→ Drag and drop your portfolio folder
→ Get instant live URL in 30 seconds
```

**2. Test Your Live Site**
```
→ Share URL with friends/colleagues
→ Test on mobile devices
→ Verify everything works
```

**3. Decide on Domain**
```
→ Free: Keep `your-name.netlify.app`
→ Paid: Buy `mikekapin.com` (~$13/year)
```

**4. (Optional) Connect Custom Domain**
```
→ Purchase domain
→ Add to Netlify
→ Wait for DNS propagation
```

---

## 📱 After Deployment

### Share Your Portfolio:
- LinkedIn profile URL
- Resume/CV
- Email signature
- GitHub profile
- Business cards

### Update Content:
- Push updates to GitHub (if using Git method)
- Or re-upload folder to Netlify (drag & drop method)
- Changes go live immediately

### Monitor:
- Netlify provides free analytics
- See page views, visitor locations
- Monitor uptime (99.9%+ guaranteed)

---

## 🎓 Your Portfolio URLs (After Deployment)

### Current (Local):
```
file:///C:/Users/m_kap/Desktop/Professional Portfolio/index.html
```

### After Netlify Deploy (Free):
```
https://mike-kapin-portfolio.netlify.app
```

### After Custom Domain (Paid):
```
https://mikekapin.com
```

---

## ✅ Ready to Deploy!

**Your portfolio includes:**
- ✅ 6 HTML pages (Home, About, Experience, Technical, LARK Labs, Contact)
- ✅ Professional styling with glass morphism design
- ✅ Responsive mobile layout
- ✅ Conference presentation photo
- ✅ Accurate project descriptions
- ✅ Contact information
- ✅ All images properly organized

**Estimated deployment time**: 15 minutes to live site
**Cost**: FREE (or $13/year with custom domain)

---

## 🆘 Need Help?

**Netlify Support**: https://docs.netlify.com
**Domain Help**: Registrar support (Namecheap, Cloudflare)
**Issues**: Check browser console for errors

---

**Ready to go live? Start here**: https://app.netlify.com 🚀

**Recommended first step**: Deploy with free Netlify subdomain, test everything, then add custom domain if desired.

