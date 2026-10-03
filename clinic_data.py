# -*- coding: utf-8 -*-
"""
Central content store for the Hariom Physio Care website.

Edit the values in this file to update the phone number, address,
timings, doctor biography, services, testimonials and blog articles —
no template changes required.
"""

DOCTOR = {
    "name": "Dr. Hariom Sharma",
    "title": "Physiotherapist",
    "degrees": "BPT, MPT (Orthopaedics)",
    "experience_years": "10+",
    "experience_line": "10+ years of clinical experience",
    "registration": "Registered Physiotherapist — State Physiotherapy & Occupational Therapy Council",
    "bio_short": (
        "Dr. Hariom Sharma is a senior physiotherapist with over a decade of hands-on "
        "experience in orthopaedic, sports and neurological rehabilitation. He is known "
        "for his patient-first approach: every treatment plan starts with listening, "
        "followed by a detailed assessment and honest, evidence-based advice."
    ),
    "bio_long": [
        "Dr. Hariom Sharma completed his Bachelor of Physiotherapy (BPT) and went on to earn a "
        "Master of Physiotherapy (MPT) specialising in Orthopaedics. Over 10+ years of practice he "
        "has treated more than 5,000 patients — from office workers with chronic back pain and "
        "athletes with ligament injuries, to seniors recovering from joint replacement surgery and "
        "stroke survivors relearning to walk.",
        "His treatment philosophy is simple: treat the person, not just the report. Dr. Sharma "
        "combines skilled manual therapy with progressive, science-backed exercise rehabilitation "
        "and modern electrotherapy modalities, and he takes the time to explain the 'why' behind "
        "every exercise so patients stay motivated and recover faster.",
        "He has completed advanced certifications in manual therapy, dry needling, kinesiology "
        "taping and sports injury rehabilitation, and regularly conducts community camps on posture, "
        "ergonomics and fall prevention for senior citizens.",
    ],
    "qualifications": [
        "Master of Physiotherapy (MPT) — Orthopaedics",
        "Bachelor of Physiotherapy (BPT)",
        "Certified Manual Therapist (Maitland Concept)",
        "Advanced Certification in Dry Needling",
        "Certified Kinesiology Taping Practitioner (KT1 & KT2)",
        "Sports Injury Rehabilitation & Return-to-Play Protocols",
    ],
    "highlights": [
        ("10+", "Years of clinical practice across hospitals and private clinics"),
        ("5,000+", "Patients successfully treated and rehabilitated"),
        ("8", "Specialised physiotherapy service areas"),
        ("4.9/5", "Average patient rating from 500+ reviews"),
    ],
    "approach": [
        ("Listen First", "Your history, lifestyle and goals shape the treatment plan — not just the X-ray report."),
        ("Assess Thoroughly", "A detailed movement and postural assessment pinpoints the true source of pain."),
        ("Treat With Evidence", "Manual therapy, exercise rehabilitation and electrotherapy — chosen from current best evidence, not trends."),
        ("Empower You", "You leave every session knowing exactly what to do at home, so recovery continues between visits."),
    ],
}

CLINIC = {
    "name": "Hariom Physio Care",
    "tagline": "Restore Movement. Rebuild Strength. Revive Life.",
    "city": "Jaipur",
    "phone": "+91 98765 43210",
    "phone_digits": "+919876543210",
    "whatsapp": "919876543210",
    "email": "hariomphysiocare@gmail.com",
    "address": "12, Health Plaza, MG Road, Malviya Nagar, Jaipur, Rajasthan 302017",
    "landmark": "Opposite City Hospital Gate No. 2",
    "hours": [
        ("Monday – Saturday", "9:00 AM – 1:00 PM"),
        ("Monday – Saturday", "5:00 PM – 9:00 PM"),
        ("Sunday", "By prior appointment only"),
    ],
    "hours_line": "Mon–Sat: 9 AM – 1 PM & 5 – 9 PM",
    "map_embed": (
        "https://www.openstreetmap.org/export/embed.html"
        "?bbox=75.7873%2C26.8510%2C75.8273%2C26.8710&layer=mapnik&marker=26.8610%2C75.8073"
    ),
    "social": {
        "facebook": "#",
        "instagram": "#",
        "youtube": "#",
    },
}

STATS = [
    ("10+", "Years Experience"),
    ("5,000+", "Patients Treated"),
    ("8", "Specialised Services"),
    ("4.9/5", "Patient Rating"),
]

SERVICES = [
    {
        "slug": "orthopedic-physiotherapy",
        "name": "Orthopedic Physiotherapy",
        "icon": "bone",
        "short": "Effective, drug-free care for back pain, neck pain, joint pain, arthritis and musculoskeletal injuries.",
        "description": [
            "Musculoskeletal pain is one of the most common reasons people lose their mobility, sleep "
            "and confidence. Whether it is a constant low-back ache, a stiff neck from long desk hours, "
            "knee pain while climbing stairs, or a frozen shoulder that will not let you sleep, "
            "orthopedic physiotherapy targets the root cause of your pain — not just the symptoms.",
            "Dr. Hariom Sharma begins every case with a detailed biomechanical assessment to identify "
            "exactly which structures are causing your problem. Your treatment plan then combines skilled "
            "hands-on manual therapy, targeted corrective exercise and modern electrotherapy modalities to "
            "relieve pain, restore mobility and rebuild the strength that keeps you pain-free long after "
            "treatment ends.",
            "Every plan also includes simple home exercises and posture or ergonomic advice, so your "
            "recovery continues between sessions.",
        ],
        "benefits": [
            "Back, neck & shoulder pain relief",
            "Knee, hip & ankle joint pain care",
            "Arthritis & spondylitis management",
            "Frozen shoulder & tendonitis treatment",
            "Sciatica & disc-related pain care",
            "Drug-free, side-effect-free recovery",
        ],
        "duration": "Typically 6–12 sessions, reviewed every 2 weeks",
    },
    {
        "slug": "sports-injury-rehabilitation",
        "name": "Sports Injury Rehabilitation",
        "icon": "dumbbell",
        "short": "Structured rehab for sprains, strains, ligament tears and overuse injuries — built to get you back to sport.",
        "description": [
            "An injury should not end your season — and rest alone is rarely rehabilitation. Dr. Sharma "
            "works with cricketers, runners, footballers, gym-goers and weekend athletes to rehabilitate "
            "injuries properly, using a staged protocol that rebuilds strength, power, agility and "
            "confidence before you return to play.",
            "From acute ankle sprains and hamstring strains to ACL reconstructions and tennis elbow, each "
            "program follows current return-to-sport criteria, not arbitrary timelines. You are progressed "
            "by objective testing, not guesswork.",
        ],
        "benefits": [
            "Acute injury management (P.R.I.C.E. protocol)",
            "ACL, meniscus & ligament injury rehab",
            "Muscle strain & tendon injury recovery",
            "Running gait analysis & retraining",
            "Sport-specific strength & conditioning",
            "Return-to-play testing & injury prevention",
        ],
        "duration": "Program staged by injury severity — from 3 weeks (sprains) to 6–9 months (ACL)",
    },
    {
        "slug": "neurological-physiotherapy",
        "name": "Neurological Physiotherapy",
        "icon": "brain",
        "short": "Specialised rehabilitation for stroke, paralysis, Parkinson's disease and nerve-related movement disorders.",
        "description": [
            "Neurological conditions change lives in an instant — but the brain and nervous system have a "
            "remarkable ability to rewire with the right training. Dr. Sharma provides structured, "
            "compassionate neurological rehabilitation for stroke survivors, patients with Parkinson's "
            "disease, spinal cord injury, facial palsy and peripheral nerve injuries.",
            "Sessions focus on retraining movement patterns, balance, gait, coordination and functional "
            "independence, using task-specific training, proprioceptive exercises and gait training with "
            "appropriate aids. Families and caregivers are trained as partners in recovery, because the "
            "work done at home is where real progress happens.",
        ],
        "benefits": [
            "Stroke & hemiplegia rehabilitation",
            "Balance training & fall prevention",
            "Gait (walking) retraining with aids",
            "Parkinson's disease exercise therapy",
            "Facial palsy & nerve injury care",
            "Caregiver training & home exercise plans",
        ],
        "duration": "Long-term programs with monthly functional reviews; home visits available",
    },
    {
        "slug": "post-surgical-rehabilitation",
        "name": "Post-Surgical Rehabilitation",
        "icon": "medcross",
        "short": "Guided recovery after knee or hip replacement, spine surgery, fracture fixation and ligament reconstruction.",
        "description": [
            "Surgery repairs the structure — rehabilitation restores the function. The outcome of a joint "
            "replacement or ligament reconstruction depends heavily on the quality of post-operative "
            "physiotherapy. Dr. Sharma follows surgeon-aligned, phase-wise protocols for every surgical "
            "rehab case.",
            "From the first gentle range-of-motion exercises to full strength and confidence on stairs, "
            "your recovery is tracked against objective milestones so you always know exactly where you "
            "stand in your journey back to normal life.",
        ],
        "benefits": [
            "Total knee & hip replacement rehab",
            "ACL / meniscus repair protocols",
            "Spine surgery recovery programs",
            "Fracture & fixation stiffness management",
            "Scar tissue mobilisation & swelling control",
            "Progressive strength & function restoration",
        ],
        "duration": "Protocol-based — typically 8–16 weeks, coordinated with your surgeon",
    },
    {
        "slug": "manual-therapy",
        "name": "Manual Therapy & Mobilisation",
        "icon": "refresh",
        "short": "Skilled hands-on techniques to unlock stiff joints, release muscle tension and restore natural movement.",
        "description": [
            "Manual therapy is the craft at the heart of physiotherapy. Using graded joint mobilisation, "
            "soft-tissue release and myofascial techniques, Dr. Sharma treats restricted joints and "
            "overworked muscles directly — often providing noticeable relief within the first few "
            "sessions.",
            "Manual therapy at Hariom Physio Care is never a stand-alone treatment. It is used to open a "
            "window of pain-free movement, which is then locked in with corrective exercise so the result "
            "lasts.",
        ],
        "benefits": [
            "Joint mobilisation & manipulation",
            "Myofascial & soft-tissue release",
            "Muscle energy techniques",
            "Trigger point & dry needling therapy",
            "Spinal mobilisation for neck & back pain",
            "Immediate pain relief to enable exercise",
        ],
        "duration": "Usually combined with exercise rehab within the same session",
    },
    {
        "slug": "electrotherapy-pain-management",
        "name": "Electrotherapy & Pain Management",
        "icon": "zap",
        "short": "Advanced IFT, ultrasound, TENS and laser therapy to reduce pain and accelerate tissue healing.",
        "description": [
            "The clinic is equipped with modern electrotherapy modalities used to calm acute pain, reduce "
            "inflammation and stimulate tissue repair — particularly valuable in the early stages of "
            "injury when exercise alone is not yet possible.",
            "Modalities are selected precisely for your diagnosis and combined with active treatment, so "
            "you are never paying for 'machine-only' sessions that produce no lasting change.",
        ],
        "benefits": [
            "Interferential therapy (IFT) for deep pain",
            "Therapeutic ultrasound for soft-tissue repair",
            "TENS-based pain relief programs",
            "Electrical muscle stimulation (EMS)",
            "Hot & cold therapy protocols",
            "Laser therapy for inflammation",
        ],
        "duration": "15–20 minute modality blocks inside a full treatment session",
    },
    {
        "slug": "home-physiotherapy",
        "name": "Home Visit Physiotherapy",
        "icon": "home",
        "short": "Clinic-quality physiotherapy at your doorstep for patients who cannot travel.",
        "description": [
            "For stroke survivors, post-surgical patients, bedridden individuals and senior citizens, "
            "travelling to a clinic can be the biggest barrier to recovery. Dr. Sharma and team bring "
            "structured physiotherapy to your home with portable equipment and a disciplined, "
            "goal-oriented program.",
            "Home sessions include the same assessment-driven approach as the clinic, plus practical "
            "training for family members — bed mobility, transfer techniques, walking aid use and home "
            "safety advice — so care continues every single day.",
        ],
        "benefits": [
            "Stroke & bedridden patient care at home",
            "Post-operative recovery without travel",
            "Senior citizen mobility & strength programs",
            "Portable treatment equipment provided",
            "Flexible morning & evening slots",
            "Family & caregiver training included",
        ],
        "duration": "Scheduled 3–5 visits per week depending on condition",
    },
    {
        "slug": "posture-ergonomics",
        "name": "Posture Correction & Ergonomics",
        "icon": "user",
        "short": "Fix tech-neck, desk-job back pain and poor posture with corrective exercise and workplace advice.",
        "description": [
            "Hours of screens, slouched sitting and forward head posture create a slow, grinding load on "
            "your neck and back. Dr. Sharma's posture program combines a detailed postural and ergonomic "
            "assessment with a corrective exercise plan that retrains the muscles holding you in poor "
            "alignment.",
            "You will also get practical, low-cost changes to your desk, phone habits and sleeping setup "
            "— because posture is a 24-hour habit, not a one-hour exercise.",
        ],
        "benefits": [
            "Desk-job & tech-neck assessment",
            "Corrective exercise programs",
            "Workstation ergonomic setup advice",
            "Scoliosis screening & exercise guidance",
            "Breathing & postural habit retraining",
            "Follow-up posture reviews",
        ],
        "duration": "4–8 week corrective program with home routine",
    },
]

WHY_CHOOSE = [
    ("award", "Qualified & Experienced", "MPT (Ortho) with 10+ years and 5,000+ patients treated across hospital and private practice."),
    ("shield", "Honest, Evidence-Based Care", "You will always be told what you need, what you don't, and when physiotherapy alone is not enough."),
    ("user", "One-Patient-at-a-Time", "No rushed queues. Every session is a dedicated, hands-on appointment with the doctor himself."),
    ("zap", "Modern Equipment", "IFT, ultrasound, TENS and laser therapy alongside progressive rehab equipment for measurable results."),
    ("heart", "Personalised Home Plans", "Simple printed & WhatsApp exercise routines keep your recovery moving between sessions."),
    ("clock", "Convenient Timings", "Morning and evening slots six days a week, plus home-visit physiotherapy for those who cannot travel."),
]

PROCESS_STEPS = [
    ("01", "Assessment", "A detailed conversation and physical examination of your movement, posture, strength and pain pattern."),
    ("02", "Diagnosis & Plan", "You receive a clear explanation of your problem and a written, goal-based treatment plan with a realistic timeline."),
    ("03", "Hands-On Treatment", "Manual therapy, electrotherapy and guided exercises — adjusted every session based on your progress."),
    ("04", "Recovery & Prevention", "Strength, mobility and habit training so the problem stays fixed, plus a home plan to protect you long-term."),
]

TESTIMONIALS = [
    {
        "name": "Ramesh Gupta",
        "condition": "Knee Osteoarthritis, Age 62",
        "text": "I had almost decided on knee replacement surgery. After three months of Dr. Hariom's exercises and therapy, I now climb two flights of stairs without support. He explains everything patiently and never rushes you.",
    },
    {
        "name": "Priya Mehta",
        "condition": "Chronic Lower Back Pain",
        "text": "Eight years of back pain from desk work, tried everything. The combination of manual therapy and his posture correction program finally gave me pain-free mornings. His home exercise sheets are simple and practical.",
    },
    {
        "name": "Amit Khandelwal",
        "condition": "ACL Reconstruction Rehab",
        "text": "As a footballer, my ACL tear felt like the end. Dr. Sharma's rehab was disciplined and scientific — every phase had clear targets. I passed my return-to-play tests at 8 months and I'm back on the field.",
    },
    {
        "name": "Sunita Agarwal",
        "condition": "Stroke Rehabilitation (family)",
        "text": "After my husband's stroke we were lost. Dr. Hariom trained us as much as he treated him — walking, transfers, exercises at home. Today he walks with a stick independently. We are forever grateful.",
    },
    {
        "name": "Vikram Singh",
        "condition": "Frozen Shoulder",
        "text": "I couldn't comb my hair or sleep on one side for months. With mobilisation and his shoulder protocol I had 80% of my movement back in six weeks. Genuinely skilled hands.",
    },
    {
        "name": "Neha Sharma",
        "condition": "Cervical Pain & Tech-Neck",
        "text": "The posture assessment was an eye-opener — he found problems I didn't even mention. Six weeks of corrective exercise plus simple desk changes and my daily headaches are gone.",
    },
]

BLOG_POSTS = [
    {
        "slug": "first-physiotherapy-visit",
        "title": "Your First Physiotherapy Visit: What to Expect",
        "category": "Patient Guide",
        "date": "12 September 2026",
        "read_time": "4 min read",
        "accent": "#0f766e",
        "excerpt": "Nervous about your first physiotherapy appointment? Here is exactly how a first consultation at Hariom Physio Care unfolds — and how to prepare for it.",
        "content": [
            ("p", "Many patients arrive at their first physiotherapy appointment unsure of what will happen. Will I be given machines? Will it hurt? Do I need a doctor's referral? This short guide removes the mystery."),
            ("h2", "1. A conversation, not a formality"),
            ("p", "Your session begins with 10–15 minutes of listening. Your physiotherapist wants the story of your pain: when it started, what makes it better or worse, how it affects sleep and daily life, and what you have already tried. Bring any reports you have — X-rays, MRIs, blood work — but know that your history matters more than your films."),
            ("h2", "2. The physical assessment"),
            ("p", "Next comes a hands-on examination. You may be asked to walk, bend, squat or lift your arm while the therapist observes your movement. Specific tests check joint mobility, muscle strength, nerve tension and posture. This is how the true source of your pain is found — it is often not where you feel it."),
            ("h2", "3. A clear explanation and plan"),
            ("p", "You should leave your first visit understanding three things: what is wrong, why it happened, and what the plan is. At Hariom Physio Care you receive a written goal-based plan with an estimated timeline, so you can judge progress objectively."),
            ("h2", "How to prepare"),
            ("list", ["Wear comfortable, loose clothing that exposes the problem area (shorts for knee pain, a vest for shoulder pain).", "Carry previous prescriptions, scans and reports.", "Note down your top 3 goals — e.g. 'sleep on my shoulder', 'climb stairs', 'sit 8 hours pain-free'.", "Arrive 10 minutes early so you are relaxed."]),
            ("p", "First visits are the foundation of recovery. Come with questions — a good physiotherapist loves answering them."),
        ],
    },
    {
        "slug": "lower-back-pain-stretches",
        "title": "5 Gentle Stretches for Lower Back Pain Relief",
        "category": "Exercise",
        "date": "28 August 2026",
        "read_time": "5 min read",
        "accent": "#b45309",
        "excerpt": "These five physiotherapist-approved movements can ease a stiff, achy lower back. Plus the two red flags that mean you should get assessed instead.",
        "content": [
            ("p", "Around 80% of people experience lower back pain at some point, and for desk-based professionals it has become almost routine. While persistent or severe pain always deserves a proper assessment, gentle movement is one of the best medicines for an ordinary stiff, achy back. Here are five movements used regularly in clinic."),
            ("h2", "1. Knee-to-chest stretch"),
            ("p", "Lie on your back, bring one knee toward your chest holding behind the thigh, and keep the other leg relaxed. Hold 20–30 seconds per side, twice each. It gently opens the lower lumbar joints."),
            ("h2", "2. Cat-camel"),
            ("p", "On hands and knees, slowly alternate between arching your back up (cat) and letting it sink down (camel). Ten slow repetitions. This is a flossing movement that lubricates the whole spine without load."),
            ("h2", "3. Child's pose"),
            ("p", "From hands and knees, sit your hips back toward your heels and reach your arms forward on the floor. Hold 30 seconds while breathing slowly. A comfortable stretch for the lower back and hips."),
            ("h2", "4. Pelvic tilts"),
            ("p", "Lying on your back with knees bent, gently flatten your lower back into the floor by tilting your pelvis, then release. Ten to fifteen repetitions. This wakes up the deep core that stabilises your spine."),
            ("h2", "5. Hamstring stretch with a towel"),
            ("p", "Lying down, loop a towel around one foot and straighten the knee until you feel a gentle pull behind the thigh. Hold 30 seconds per side. Tight hamstrings quietly increase load on the lower back."),
            ("h2", "When stretching is not enough"),
            ("p", "See a physiotherapist promptly if your pain travels below the knee, causes numbness or weakness, disturbs sleep every night, or follows a fall. Those are not 'stretch it out' signs — they are 'get assessed' signs."),
        ],
    },
    {
        "slug": "desk-posture-guide",
        "title": "The Desk Worker's Posture Survival Guide",
        "category": "Ergonomics",
        "date": "10 August 2026",
        "read_time": "6 min read",
        "accent": "#0369a1",
        "excerpt": "Tech-neck, tight hips and a dull afternoon backache — sound familiar? A physiotherapist's practical fixes for the modern desk setup.",
        "content": [
            ("p", "The human body was designed to move, and the modern desk job asks it to hold one shape for nine hours. The result is the familiar pattern we see every week in clinic: forward head ('tech-neck'), rounded shoulders, tight hip flexors and a dull lower-back ache that appears every afternoon. The good news: small, cheap changes fix most of it."),
            ("h2", "Set your screen right"),
            ("p", "The top third of your screen should sit at eye level. Every centimetre your head drifts forward multiplies the load on your neck — at a typical slouch, your neck muscles can be carrying the equivalent of 25–30 kg. Raise the laptop on a stack of books and use an external keyboard; it is the highest-return ergonomics investment there is."),
            ("h2", "Elbows, hips, feet"),
            ("p", "Elbows at roughly 90 degrees with shoulders relaxed, hips slightly above knees, and feet flat on the floor or a footrest. If your chair fights you, add a small cushion behind the lumbar curve."),
            ("h2", "The best posture is the next posture"),
            ("p", "No position is healthy for eight hours — even a 'perfect' one. The real enemy is stillness. Set a 40-minute timer: stand, walk ten steps, do five shoulder rolls. Movement snacks beat marathon stretching sessions."),
            ("h2", "Three daily reset exercises"),
            ("list", ["Chin tucks: 10 slow repetitions, drawing the head back over the shoulders.", "Doorway chest stretch: 30 seconds per side to undo the slouch.", "Hip flexor stretch: 30 seconds per side in a half-kneeling lunge."]),
            ("p", "If your neck or back still aches daily despite a good setup, the issue is usually weak postural endurance muscles — and that is exactly what a structured corrective program fixes. That is a solvable problem, not a life sentence."),
        ],
    },
    {
        "slug": "sports-injury-dos-donts",
        "title": "Sports Injury Recovery: The Do's and Don'ts",
        "category": "Sports Rehab",
        "date": "22 July 2026",
        "read_time": "5 min read",
        "accent": "#7c3aed",
        "excerpt": "Rushing back too soon re-injures; resting too long weakens. A physiotherapist's rules for recovering from a sports injury the right way.",
        "content": [
            ("p", "Every sports season produces the same two mistakes: athletes who return too early and re-tear, and athletes who rest for months and return weak, cautious and deconditioned. Rehabilitation is neither — it is a structured bridge between injury and performance."),
            ("h2", "Do's"),
            ("list", [
                "Do respect the first 48–72 hours: protect, ice, compress and elevate to control the initial inflammatory storm.",
                "Do get an accurate diagnosis early — a 'sprain' that is actually a grade-2 ligament tear needs a very different plan.",
                "Do keep training what is not injured. Cardio, core and the opposite limb can usually be trained safely and dramatically shorten overall comeback time.",
                "Do progress by criteria, not calendar: pain-free strength, full range of motion and successful hop/agility tests before return to sport.",
                "Do sleep like it is part of training — because tissue repair literally happens while you sleep.",
            ]),
            ("h2", "Don'ts"),
            ("list", [
                "Don't judge recovery by pain alone. Pain settles long before tissue regains full strength.",
                "Don't jump straight back into match intensity — the re-injury risk is highest in the first weeks after return.",
                "Don't rely only on painkillers to play through injury; masking pain does not stabilise a joint.",
                "Don't copy someone else's rehab video. Two ACL tears can need two different programs.",
            ]),
            ("p", "The goal of rehabilitation is not just to heal the injury but to return you stronger than before it. Done properly, a well-rehabbed athlete often comes back with better movement quality than pre-injury — that is the silver lining worth aiming for."),
        ],
    },
]

TIME_SLOTS = [
    "09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
    "12:00 PM", "12:30 PM", "05:00 PM", "05:30 PM", "06:00 PM", "06:30 PM",
    "07:00 PM", "07:30 PM", "08:00 PM", "08:30 PM",
]

FAQS = [
    ("Do I need a doctor's referral for physiotherapy?",
     "No. In India physiotherapists are first-contact practitioners — you can consult directly. If your condition needs a physician's opinion, Dr. Sharma will refer you appropriately."),
    ("How long is each session?",
     "A typical treatment session lasts 40–60 minutes, including assessment, hands-on treatment and guided exercise. First consultations take about 60 minutes."),
    ("How many sessions will I need?",
     "It depends on your condition. Acute problems often improve in 4–8 sessions; post-surgical and neurological rehabilitation follows longer, protocol-based timelines. You receive an estimated plan at your first visit."),
    ("Does physiotherapy hurt?",
     "Treatment should not be sharply painful. Some techniques produce a mild, comfortable stretch or soreness that settles quickly. Intensity is always guided by your feedback."),
    ("Do you provide home physiotherapy?",
     "Yes. Home visits are available for stroke patients, post-surgical patients, senior citizens and anyone unable to travel, with portable equipment and caregiver training included."),
    ("What should I wear to my appointment?",
     "Comfortable, loose clothing that allows the problem area to be examined — for example shorts for knee pain or a sleeveless top for shoulder pain."),
]
