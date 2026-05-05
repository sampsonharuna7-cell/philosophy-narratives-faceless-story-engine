def generate_philosophy_script(topic, style="Stoic", length="20s"):
    """
    Generates a short-form philosophy reel script with tight pacing.
    Returns: dict with hook options, voiceover, on-screen text, visuals, CTA, hashtags.
    """

    hook_options = [
        f"The internet is loud. {topic} is quiet.",
        f"If {topic} matters, why do we live like it doesn’t?",
        f"You don’t need more motivation. You need {topic}.",
    ]

    # Core voiceover (tight lines)
    voiceover = [
        f"In {topic}, the goal isn’t control. It’s clarity.",
        "You can’t choose the noise.",
        "But you can choose your attention.",
        "What steals your peace is never worth your time.",
        "Discipline is freedom, repeated daily."
    ]

    # On-screen text mirrors voiceover but even shorter
    on_screen_text = [
        f"{topic}",
        "Noise is external.",
        "Attention is yours.",
        "Protect your peace.",
        "Discipline = Freedom."
    ]

    visuals = [
        "High-contrast slow clouds or drifting smoke",
        "Minimalist silhouette scrolling a phone",
        "Cut to stillness: closed eyes, slow breath",
        "Final frame: simple black background with white text"
    ]

    cta = "Follow for daily philosophy you can use."

    hashtags = ["#stoicism", "#philosophy", "#selfmastery", "#discipline", "#mindset"]

    return {
        "topic": topic,
        "hook_options": hook_options,
        "voiceover": voiceover,
        "on_screen_text": on_screen_text,
        "visuals": visuals,
        "cta": cta,
        "hashtags": hashtags,
    }

if __name__ == "__main__":
    script = generate_philosophy_script("Stoicism in the Digital Age")
    print("HOOK IDEAS:")
    print("\n".join(script["hook_options"]))
    print("\nVOICEOVER:")
    print("\n".join(script["voiceover"]))
    print("\nON SCREEN TEXT:")
    print("\n".join(script["on_screen_text"]))
    print("\nVISUALS:")
    print("\n".join(script["visuals"]))
    print("\nCTA:")
    print(script["cta"])
    print("\nHASHTAGS:")
    print(" ".join(script["hashtags"]))
