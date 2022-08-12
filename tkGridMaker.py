#keep all your buttons, labels, entry boxes, etc. 2 letter vars so looks nicer (aka easier to construct the UI)
#make the UI variables here into strings because 1) we treat them as strings in the function and 2) It spaces the array more nicely
#this assumes each UI element has a unique variable name. So if you want to use the same thing twice, like the label text "hi I'm George" then use two different variables l1 l2 rather than just l1 (probably should do that anyway)
#The '00' here are placeholders i.e. empty portions of the app
gridArray = [
    [ 't1', '00', 'h1' ],
    [ 'd3', 'd4', 'd5' ],
    [ 'b2', 'e1', 'b1' ],
    [ 'l1', 'd1', '00' ],
    [ 'l2', 'd2', '00' ],
    [ 'GD', '00', 'b3' ]
]

def gridPlacer(gridArray, emptyEntity = '00', default_padx=0, default_pady=0):
    UIentityList = [item for sublist in gridArray for item in sublist] #flattened the grid

    while emptyEntity in UIentityList:
        UIentityList.remove(emptyEntity) #remove placeholder emptyEntity 

    constructionString = ''

    if len(UIentityList) == 0:
        return "No UI elements found"

    for i in UIentityList:
        coordinateTuple = [(index, row.index(i)) for index, row in enumerate(gridArray) if i in row][0] #(row, column) coordinate tuple
        
        constructionString = constructionString + f"{i}.grid(row={coordinateTuple[0]}, column={coordinateTuple[1]}, padx={default_padx}, pady={default_pady})" + "\n"
    
    print(constructionString) #this is actual code output

    return constructionString

gridPlacer(gridArray, emptyEntity = '00', default_padx=60, default_pady=60 )
