import data
def main():
    ubike:list[dict] = data.load_data()
    print(ubike)

if __name__ == '__main__':
    main()