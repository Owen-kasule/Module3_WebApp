# 📹 Module 3 - 1 Minute Video Demo Script

## 🎬 TIMING: 60 seconds (1 minute)

---

## 🎯 OPENING (0:00 - 0:05) - 5 seconds

**[Screen: VS Code or Terminal]**

**YOU SAY:**
> "Hello! This is my Module 3 Django web application for SoundHire - a sound equipment rental booking system with Supabase database integration."

**ACTION:**
- Show your face or just speak clearly
- Have the terminal ready with the project folder open

---

## 💻 SCENE 1: Start Server (0:05 - 0:10) - 5 seconds

**[Screen: Terminal]**

**YOU SAY:**
> "Let me start the Django development server."

**ACTION:**
```bash
cd "/home/kasule/Documents/2025 Semester Winter/CSE 310: Applied Programming/SoundHire/Module3_WebApp"
python manage.py runserver
```

**WHAT TO SHOW:**
- Type the commands (or have them ready to paste)
- Wait for "Starting development server at http://127.0.0.1:8000/"

---

## 🏠 SCENE 2: Homepage with Packages (0:10 - 0:25) - 15 seconds

**[Screen: Browser at http://127.0.0.1:8000/]**

**YOU SAY:**
> "Here's the homepage showing three equipment packages pulled from Supabase - Basic, Standard, and Premium. Notice the modern black and white design. Each package displays its price and description from the database."

**ACTION:**
1. Open browser to http://127.0.0.1:8000/
2. Slowly scroll to show the hero section
3. Point out the three package cards in grayscale gradients
4. Scroll down to show the booking form

**WHAT TO SHOW:**
- ✅ Hero section with title
- ✅ Three package cards (different gray gradients)
- ✅ Prices displayed (UGX amounts)
- ✅ Booking form visible below

---

## 📝 SCENE 3: Create Booking (0:25 - 0:35) - 10 seconds

**[Screen: Still on homepage, booking form section]**

**YOU SAY:**
> "Now I'll create a booking by filling out the form with customer details."

**ACTION:**
1. Scroll to booking form
2. **QUICKLY** fill out:
   - Name: "Demo User"
   - Email: "demo@test.com"
   - Phone: "+256700000000"
   - Event Date: (pick any future date)
   - Package: "Standard Sound Package"
   - ✅ Check "Include DJ Service"
   - Notes: "Demo booking"
3. Click "Submit Booking Request"

**WHAT TO SHOW:**
- Form fields being filled
- Click submit button
- Wait for success page

---

## ✅ SCENE 4: Success Page (0:35 - 0:40) - 5 seconds

**[Screen: Booking success page]**

**YOU SAY:**
> "The booking is confirmed and saved to the Supabase database."

**ACTION:**
- Show the success page with checkmark
- Point out customer name displayed
- Show "What happens next" section

**WHAT TO SHOW:**
- ✅ Success icon
- ✅ Customer name confirmation
- ✅ Booking details

---

## 🔐 SCENE 5: Admin Login (0:40 - 0:45) - 5 seconds

**[Screen: Browser]**

**YOU SAY:**
> "Now let me access the admin dashboard."

**ACTION:**
1. Navigate to: http://127.0.0.1:8000/admin/login/
2. Enter access code: `soundhire-admin-2025`
3. Click "Login"

**WHAT TO SHOW:**
- Login form
- Type access code (you can blur it in editing if needed)
- Click login button

---

## 📊 SCENE 6: Admin Dashboard (0:45 - 0:55) - 10 seconds

**[Screen: Admin dashboard]**

**YOU SAY:**
> "The admin dashboard shows all bookings from the database. I can filter by status and take actions like confirming or canceling bookings."

**ACTION:**
1. Show the statistics cards at top (Total, Pending, Confirmed, Revenue)
2. Scroll down to show bookings table
3. Try the status filter dropdown (switch to "pending")
4. Show the Confirm/Cancel buttons on a booking row

**WHAT TO SHOW:**
- ✅ Summary statistics cards
- ✅ Bookings table with data
- ✅ Filter dropdown
- ✅ Action buttons (Confirm/Cancel)
- ✅ Booking details in table

---

## 🎬 CLOSING (0:55 - 1:00) - 5 seconds

**[Screen: Still on dashboard OR switch to code view]**

**YOU SAY:**
> "This application demonstrates four dynamic pages with complete database integration using Django and Supabase. Thank you!"

**ACTION:**
- Quick switch to show code editor with files (optional)
- Or just stay on dashboard

**WHAT TO SHOW:**
- Final view of working application
- Smile! 😊

---

## 🎥 RECORDING TIPS

### Before Recording:

1. **Clear browser data** to show fresh demo
2. **Close unnecessary tabs** and applications
3. **Set browser zoom to 100%**
4. **Prepare commands in a text file** to copy/paste quickly
5. **Test the flow once** before recording
6. **Check audio levels**

### Recording Setup:

**Option A: Use OBS Studio (Free)**
```bash
# Install OBS Studio
sudo dnf install obs-studio  # Fedora/RHEL
# Or download from: https://obsproject.com/
```

**Option B: Use SimpleScreenRecorder (Linux)**
```bash
sudo dnf install simplescreenrecorder
```

**Option C: Use Browser extension**
- Loom (free, easy): https://loom.com
- Screencastify

### Recording Settings:

- **Resolution**: 1920x1080 (1080p) or 1280x720 (720p)
- **Frame Rate**: 30 fps
- **Audio**: Built-in microphone (test first!)
- **Cursor**: Make it visible and larger if possible

### During Recording:

1. ✅ Speak clearly and at moderate pace
2. ✅ Move mouse slowly and deliberately
3. ✅ Pause briefly between scenes
4. ✅ If you make a mistake, just restart - 1 minute is quick!
5. ✅ Smile (even if not showing face - it affects your voice!)

### After Recording:

1. **Watch it once** to check:
   - ✅ Audio is clear
   - ✅ All features shown
   - ✅ No sensitive information visible (passwords, keys)
   - ✅ Timing is close to 60 seconds (50-70 seconds is fine)

2. **Upload to YouTube:**
   - Set title: "CSE 310 Module 3 - Django Web Application Demo"
   - Set visibility: Unlisted or Public
   - Copy the link for Canvas submission

---

## 📋 QUICK CHECKLIST BEFORE RECORDING

Print this and check off:

- [ ] Server starts successfully
- [ ] Homepage loads with 3 packages
- [ ] Booking form works
- [ ] Success page appears after submission
- [ ] Admin login works (code: soundhire-admin-2025)
- [ ] Dashboard shows bookings
- [ ] Filter dropdown works
- [ ] Audio equipment tested
- [ ] Screen recorder ready
- [ ] Browser set to 100% zoom
- [ ] Unnecessary tabs closed
- [ ] Script reviewed

---

## 🎯 ALTERNATIVE 30-SECOND SPEED VERSION

If you want to make it SUPER quick (30 seconds):

**0:00-0:05** - "Module 3 Django app. Starting server..." [show terminal]
**0:05-0:15** - "Homepage with packages from Supabase database" [show homepage, scroll quickly]
**0:15-0:20** - "Submitting a booking..." [fill form fast, submit]
**0:20-0:25** - "Admin dashboard shows all bookings..." [login quickly, show dashboard]
**0:25-0:30** - "Complete with filtering and actions. Thank you!" [show filter, done]

---

## 💡 PRO TIPS

1. **Practice makes perfect** - Do a test recording first
2. **Don't worry about perfection** - Natural is better than scripted
3. **Energy matters** - Sound enthusiastic about your work!
4. **If you mess up** - Just start over, it's only 1 minute
5. **Background music** - Optional, but keep it VERY quiet
6. **Captions** - YouTube auto-generates them, review and fix if needed

---

## 🚨 COMMON MISTAKES TO AVOID

❌ Talking too fast (slow down!)
❌ Not showing the URL bar (so viewers can see it's real)
❌ Forgetting to show database-driven content
❌ Not demonstrating admin features
❌ Audio too quiet or too loud
❌ Screen too small or zoomed in
❌ Showing .env file with credentials
❌ Video longer than 90 seconds

---

## ✅ YOU'RE READY!

Take a deep breath, hit record, and follow the script. You've got this! 🚀

**Good luck with your demo video!** 🎬
