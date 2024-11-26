def mini_game(building):
    """
    calls the mini-game for each respective building
    """
    if building == "library":
        # call library game function
        pygame.mixer.music.load('music/lofi2.mp3')
        pygame.mixer.music.play(-1)
        pass
    elif building == "cafeteria":
        # call cafeteria game function
        pygame.mixer.music.load('music_assets/battle.mp3')
        pygame.mixer.music.play(-1)
        pass
    elif building == "counselling_office":
        # call counselling game function
        pygame.mixer.music.load('music_assets/chill.mp3')
        pygame.mixer.music.play(-1)
        pass
    elif building == "classroom":
        # call classroom game function
        pygame.mixer.music.load('music_assets/lofi3.mp3')
        pygame.mixer.music.play(-1)
        pass
    elif building == "it_dept":
        # call it game function
        pygame.mixer.music.load('music_assets/lofi4.mp3')
        pygame.mixer.music.play(-1)
        pass