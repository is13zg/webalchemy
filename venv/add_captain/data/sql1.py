def main():
    global_init(input())

    session = create_session()
    # session.add(user)
    for user in session.query(User).filter(User.address == "module_1"):
        print(user)


if __name__ == '__main__':
    main()
