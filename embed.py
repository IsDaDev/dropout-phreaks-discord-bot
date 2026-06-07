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
    return discord.Embed(
        title="List of Certificates sorted by Domain",
        description=(
            "[PaulJeremy Certificate Roadmap](https://pauljerimy.com/security-certification-roadmap/)"
        ),
        color=discord.Color.green()
    )

def resourcesembed():
    embed = discord.Embed(
        title="List of Cybersecurity Resources",
        description="A curated list of learning platforms, networking, OS fundamentals, hacking, reverse engineering, and blue teaming resources.",
        color=discord.Color.orange()
    )
    embed.add_field(
        name="🧪 Practice Platforms",
        value=(
            "• [HackTheBox](https://www.hackthebox.eu/)\n"
            "• [TryHackMe](https://tryhackme.com/)\n"
            "• [List of 350 free THM Rooms](https://github.com/uttambodara/TryHackMeRoadmap)\n"
            "• [PicoCTF](https://www.picoctf.org/)"
        ),
        inline=False
    )

    embed.add_field(
        name="Guides",
        value=(
            "• [Roadmap.sh Cybersecurity](https://roadmap.sh/cyber-security)\n"
            "• [Getting started guide by IsDaDev](https://www.isdadev.at/posts/getting-started/)\n"
            "• [Hacktricks Wiki](https://hacktricks.wiki/)\n"
            "• [Red Team Notes](http://ired.team/)\n"
            "• [HackTheBox Beginners Bible](https://www.hackthebox.com/blog/learn-to-hack-beginners-bible)"
        ),
        inline=False
    )

    embed.add_field(
        name="🌐 Networking",
        value=(
            "• [Cisco NetAcad: Networking Basics](https://www.netacad.com/courses/networking-basics?courseLang=en-US)\n"
            "• [ZeroToMastery: Intro to Networking](https://zerotomastery.io/blog/introduction-to-networking/)"
        ),
        inline=False
    )
    embed.add_field(
        name="🐧 Linux / CLI",
        value=(
            "• [OverTheWire: Bandit](https://overthewire.org/wargames/)\n"
            "• [LinuxJourney](https://linuxjourney.com/)"
        ),
        inline=False
    )
    embed.add_field(
        name="🪟 Windows / Active Directory",
        value=(
            "• [TryHackMe: Windows Fundamentals](https://tryhackme.com/module/windows-fundamentals)\n"
            "• [Sophos: What is Active Directory](https://www.sophos.com/en-us/cybersecurity-explained/active-directory-security)\n"
            "• [JustHacking: Windows Internals (Shikata)](https://learn.justhacking.com/courses/8c15538d-d3d2-4b02-b95f-958bece398c0)\n"
            "• [Attacking AD by zer1t0](https://zer1t0.gitlab.io/posts/attacking_ad/#why-this-post)"
        ),
        inline=False
    )
    embed.add_field(
        name="🕸️ Web Hacking",
        value=(
            "• [PortSwigger Web Security Academy](https://portswigger.net/web-security/learning-paths)"
        ),
        inline=False
    )
    embed.add_field(
        name="🧩 Reverse Engineering, pwn",
        value=(
            "• [0xInfection: Reverse Engineering Guide](https://0xinfection.github.io/reversing/)\n"
            "• [guyinatuxedo: Nighmare, RE and pwn for CTFs](https://guyinatuxedo.github.io/index.html)\n"
            "• [PicoCTF Reverse Engineering Primer](https://primer.picoctf.org/)\n"
            "• [pwn.college](https://pwn.college/)\n"
            "• [pwnable.kr](https://pwnable.kr/)\n"
            "• [rootme](https://www.root-me.org/)\n"
            "• [pwn-notes by sashactf](https://sashactf.gitbook.io/pwn-notes)\n"
            "• [Reverse Engineering Fundamentals by 3ch0](https://www.notion.so/3ch0/Reverse-Engineering-Fundamentals-297d05a447d580f6bf19f1e1248473e1)"
        ),
        inline=False
    )
    embed.add_field(
        name="👾 Malware",
        value=(
            "• [Awesome Malware Analysis by rshipp](https://github.com/rshipp/awesome-malware-analysis)\n"
            "• [Practical Malware Analysis (book)](https://www.kea.nu/files/textbooks/humblesec/practicalmalwareanalysis.pdf)"
            "• [Malware Development by 0xpat](https://0xpat.github.io/Malware_development_part_1/)\n"
            "• [Historical Resources for Malware](http://textfiles.com/virus/)"
        ),
        inline=False
    )
    embed.add_field(
        name="🛡️ Blue Team / Defensive Security",
        value=(
            "• [Blueteam homelabs](https://github.com/aboutsecurity/blueteam_homelabs)\n"
            "• [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response)\n"
            "• [Blueteamlabs](https://blueteamlabs.online/)\n"
            "• [Orange Book Blackhillsec (IR)](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-infosec-survival-guide-orange-book/)"
        ),
        inline=False
    )
    embed.add_field(
        name="🔗 Additional Resources",
        value=(
            "• [Acid.Wiki](https://acid.wiki/)\n"
            "• [Daniel Miessler: Infosec Career Guide](https://danielmiessler.com/blog/build-successful-infosec-career/)\n"
            "• [100 Red-Team Projects](https://github.com/kurogai/100-redteam-projects)\n"
            "• [Historical Resources for Hacking](http://textfiles.com/hacking/)\n"
            "• [Phineas Fisher hack documentations](https://theanarchistlibrary.org/category/author/phineas-fisher)"
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
        name="",
        value="You have been pinged since you asked to ask a question. It might be better to just ask what you want to know. " \
        "So instead of asking \"Hey any Java expert here?\", you could ask \"I got a problem with x using Java and I would be " \
        "glad if somebody could help me find a solution\". Also including information on what you have tried or done already can " \
        "be really helpful.",
        inline=False
    )
    dataembed.add_field(
        name="Read More",
        value="https://dontasktoask.com/",
        inline=False
    )
    dataembed.add_field(
        name="The art of asking better questions",
        value="https://medium.com/@rickharrison_/the-art-of-asking-better-questions-4312b5d469e0",
        inline=False
    )
    return dataembed

# class VoteState:
#     def __init__(self):
#         self.counter = 0
#         self.voters = set()

# async def button(interaction: discord.Interaction, user, votes: int = 10, requires_regular_or_higher: bool = False):
#     vote_state = VoteState()

#     view = discord.ui.View()
#     vote = discord.ui.Button(label="Vote to ban", style=discord.ButtonStyle.primary)
#     cancel = discord.ui.Button(label="Cancel vote", style=discord.ButtonStyle.danger)

#     async def voteButtonClick(interaction: discord.Interaction):
#         if requires_regular_or_higher:
#             userrole = interaction.user.roles                                         
#             if not any(role.id in [514593949503979530, # root
#                                    557638531871146000, # sudoers
#                                    557639875440934932, # legend 
#                                    1162203070978068530, # regularbutbetter and regular at the bottom
#                                    557639177169010688] for role in userrole):
#                 await interaction.response.send_message("This vote is only for regular and higher!", ephemeral=True)
#                 return

#         if interaction.user.id in vote_state.voters:
#             await interaction.response.send_message("You have already voted!", ephemeral=True)
#             return
        
#         vote_state.counter += 1
#         vote_state.voters.add(interaction.user.id)
#         await interaction.response.send_message(f"You voted to ban {user}!", ephemeral=True)
        
#         if vote_state.counter == votes:
#             await interaction.message.edit(content=f"{user} has been banned!", view=None)
#             await interaction.guild.ban(user)

#     async def cancelVote(interaction: discord.Interaction):
#         userrole = interaction.user.roles
#         if not any(role.id in [514593949503979530, 557638531871146000] for role in userrole):
#             await interaction.response.send_message("You don't have permission to cancel this vote!", ephemeral=True)
#             return
    
#         await interaction.message.edit(content=f"The vote to ban {user} has been cancelled!", view=None)

#     vote.callback = voteButtonClick
#     cancel.callback = cancelVote
#     view.add_item(vote)
#     view.add_item(cancel)

#     await interaction.response.send_message(f"Vote to ban the user {user}!", view=view)