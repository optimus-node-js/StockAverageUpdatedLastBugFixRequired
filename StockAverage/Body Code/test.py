if exists('averageData.json'):
    '''Inserting Data in Existing JSON File'''

    with open("averageData.json", 'r+') as file:
        file_data = load(file)
        file_data['averageData'].append(data)
        file.seek(0)
        dump(file_data, file, indent=4)

        '''Collection Stored in Server'''
        collectionI = dbI['averageData']
        collectionI.insert_one(data)


else:
    Attribute = {
        "averageData": []
    }
    with open("averageData.json", "w") as file:
        json_object = dumps(Attribute, indent=4)
        file.write(json_object)

    '''We are Inserting Server All Data in JSON Files.'''
    call(["attrib", "+h", "/s", "/d", "averageData.json"])

    _collection = dbI["averageData"].find({}, {"_id": 0})

    newData = [item for item in _collection]
    newData.append(data)

    for item in newData:
        with open("averageData.json", 'r+') as file:
            file_data = load(file)
            file_data['averageData'].append(item)
            file.seek(0)
            dump(file_data, file, indent=4)

    '''Inserting data in Server'''
    _collection = dbI['averageData']
    _collection.insert_one(data)
