def main():
    block_list = "refined-blacklist.txt"
    host_list = "refined-blacklist-hosts"
    with open(block_list) as file:
        sites = file.readlines()

    with open(host_list, "w") as file:
        for line in sites:
            host_append = "127.0.0.1 " + line
            file.writelines(host_append)




if __name__ == "__main__":
    main()