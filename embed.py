import discord

def hdigsembed():
    hdigsembed = discord.Embed(
        title="Getting started in cybersecurity",
        description=(
            "Don't rush straight into hacking tools or labs.\n"
            "If you're new to cybersecurity (or IT in general), "
            "building a strong foundation first will save you a lot of frustration later."
        ),
        color=discord.Color.blurple()
    )

    hdigsembed.add_field(
        name="Core foundations",
        value=(
            "• **Networking** — how systems communicate (most important)\n"
            "• **Linux basics** — most servers and tools run on Linux\n"
            "• **Web basics** — if you want to get into websites, you have to understand how a website works\n"
            "• **Windows fundamentals** — especially Active Directory\n"
            "• **Programming / scripting** — not mandatory, but automation helps"
        ),
        inline=False
    )

    hdigsembed.add_field(
        name="Why this matters",
        value=(
            "You can't secure or break systems without understanding how they work.\n"
            "Most attacks and defenses rely on networking and OS knowledge."
        ),
        inline=False
    )

    hdigsembed.add_field(
        name="What comes next",
        value=(
            "Practice on CTF platforms like:\n"
            "• Hack The Box\n"
            "• TryHackMe"
        ),
        inline=False
    )

    hdigsembed.add_field(
        name="🔗 Resources",
        value=(
            "[Getting Started Guide isdadev.at](https://www.isdadev.at/posts/getting-started/)\n"
            "[Longer version of this post](https://discord.com/channels/326839256758616068/1397957109064405053)"
        ),
        inline=False
    )

    hdigsembed.add_field(
        name="Happy learning!",
        value="More resources are listed in the `/resources` command."
    )

    return hdigsembed

def igothackedembed():
    igothackedembed = discord.Embed(
        title="What to do if you get hacked",
        description=(
            "If you suspect your account or system has been compromised, act quickly:\n"
            "1. Change passwords immediately\n"
            "2. Enable multi-factor authentication (MFA)\n"
            "3. Scan for malware and remove any threats\n"
            "4. Review account activity for unauthorized actions\n"
            "5. Inform relevant parties (employer, bank, etc.)\n"
            "6. Consider professional help if needed"
        ),
        color=discord.Color.red()
    )

    igothackedembed.add_field(
        name="Stay Calm",
        value="Panicking can lead to mistakes. Take a deep breath and follow the steps methodically.",
        inline=False
    )

    igothackedembed.add_field(
        name="Prevention Tips",
        value=(
            "• Regularly update software and systems\n"
            "• Use strong, unique passwords\n"
            "• Use 2 Factor Authentication wherever it is possible\n"
            "• Be cautious of phishing attempts\n"
            "• Backup important data frequently"
        ),
        inline=False
    )

    return igothackedembed

def certificatesembed():
    certificatesembed = discord.Embed(
        title="List of Certificates sorted by Domain",
        description=(
            "[PaulJeremy Certificate Roadmap](https://pauljerimy.com/security-certification-roadmap/)"
        ),
        color=discord.Color.green()
    )

    return certificatesembed

import discord

def resourcesembed():
    embed = discord.Embed(
        title="List of Cybersecurity Resources",
        description="A curated list of learning platforms, networking, OS fundamentals, hacking, reverse engineering, and blue teaming resources.",
        color=discord.Color.orange()
    )

    # Practice Platforms
    embed.add_field(
        name="🧪 Practice Platforms",
        value=(
            "• [Hack The Box](https://www.hackthebox.eu/)\n"
            "• [TryHackMe](https://tryhackme.com/)\n"
            "• [PicoCTF](https://www.picoctf.org/)"
        ),
        inline=False
    )

    # Networking
    embed.add_field(
        name="🌐 Networking",
        value=(
            "• [Cisco NetAcad: Networking Basics](https://www.netacad.com/courses/networking-basics?courseLang=en-US)\n"
            "• [ZeroToMastery: Intro to Networking](https://zerotomastery.io/blog/introduction-to-networking/)"
        ),
        inline=False
    )

    # Linux / CLI
    embed.add_field(
        name="🐧 Linux / CLI",
        value=(
            "• [OverTheWire: Bandit](https://overthewire.org/wargames/)\n"
            "• [LinuxJourney](https://linuxjourney.com/)"
        ),
        inline=False
    )

    # Windows / AD
    embed.add_field(
        name="🪟 Windows / Active Directory",
        value=(
            "• [TryHackMe: Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals)\n"
            "• [Sophos: What is Active Directory](https://www.sophos.com/en-us/cybersecurity-explained/active-directory-security)\n"
            "• [JustHacking: Windows Internals (Shikata)](https://learn.justhacking.com/courses/8c15538d-d3d2-4b02-b95f-958bece398c0)"
        ),
        inline=False
    )

    # Web Hacking
    embed.add_field(
        name="🕸️ Web Hacking",
        value=(
            "• [PortSwigger Web Security Academy](https://portswigger.net/web-security/learning-paths)"
        ),
        inline=False
    )

    # Reverse Engineering
    embed.add_field(
        name="🧩 Reverse Engineering, pwn",
        value=(
            "• [0xInfection: Reverse Engineering Guide](https://0xinfection.github.io/reversing/)\n"
            "• [PicoCTF Reverse Engineering Primer](https://primer.picoctf.org/)\n"
            "• [pwn.college](https://pwn.college/)"
        ),
        inline=False
    )

    embed.add_field(
        name="👾 Malware Reverse Engineering",
        value=(
            "• [Awesome Malware Analysis by rshipp](https://github.com/rshipp/awesome-malware-analysis)\n"
            "• [Practical Malware Analysis (book)](https://www.kea.nu/files/textbooks/humblesec/practicalmalwareanalysis.pdf)"
        ),
        inline=False
    )

    # Blue Teaming
    embed.add_field(
        name="🛡️ Blue Team / Defensive Security",
        value=(
            "• [Blueteam homelabs](https://github.com/aboutsecurity/blueteam_homelabs)\n"
            "• [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response)\n"
            "• [Blueteamlabs](https://blueteamlabs.online/)"
        ),
        inline=False
    )

    embed.add_field(
        name="🔗 Additional Resources",
        value=(
            "• [Acid.Wiki](https://acid.wiki/)\n"
            "• [Daniel Miessler: Infosec Career Guide](https://danielmiessler.com/blog/build-successful-infosec-career/)\n"
            "• [100 Red-Team Projects](https://github.com/kurogai/100-redteam-projects)"
        ),
        inline=False
    )

    return embed

def blogembed():
    blogembed = discord.Embed(
        title="Acid.wiki Blog",
        description=(
            "Check out the latest articles and updates on cybersecurity at the Acid.wiki blog."
        ),
        color=discord.Color.purple()
    )

    blogembed.add_field(
        name="🔗 Blog Link",
        value="[Acid.wiki Blog](https://acid.wiki/blog)",
        inline=False
    )

    return blogembed

def dontasktoaskembed():
    dataembed = discord.Embed(
        title="Don't Ask To Ask",
        color=discord.Color.dark_gold()
    )

    dataembed.add_field(
        value="[Don't ask to ask](https://dontasktoask.com/)",
        inline=False
    )

    return dataembed