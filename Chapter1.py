ready = input("===================\nAdventureGames\n===================\nGithub: https://github.com/Kylan1940\n===================\nAre you ready? (y/n)")

if (ready == "y"){
print("--== COMING SOON ==--")
}

if (ready == "n"){
quit()
}

if (ready != "y" && ready != "n"){
print("Please write 'y' or 'n'")
}