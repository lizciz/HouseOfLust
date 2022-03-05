init python:

    # Helper function for showing kitchen table.
    # vars c1-c4 will be shown in order. If set to none, empty chair will be shown.
    # Chair orders are: back, left, right, front
    def kitchen_table_setup(order = [], images = {}):
        defaultOrder = [
            "table",
            "c1",
            "c2",
            "c3",
            "c4",
            "ontop",
        ]
        defaultImages = {
            "table" : None,
            "c1" : None,
            "c2" : None,
            "c3" : None,
            "c4" : None,
            "ontop" : None,
        }
        _order = unique(order + defaultOrder)
        print(_order)
        _images = {}
        _images.update(defaultImages)
        _images.update(images)

        for pos in _order:
            img = _images[pos]
            displayable = kitchen_table_helper(pos, img)
            if displayable is not None:
                renpy.show(displayable, tag=pos)
    
    def kitchen_table_helper(pos, img):
        if pos in ["c1","c2","c3","c4"]:
            posName = kitchen_table_poss(pos)
            if img is None:
                return "kitchen_table chair_{} in".format(posName)
            elif img is "in" or img is "out":
                return "kitchen_table chair_{} {}".format(posName, img)
            else:
                return img
            return pos
        elif pos == "table":
            return "kitchen_table nochairs empty"
        elif pos == "ontop" and img is not None:
            return img
        
        return None

    def kitchen_table_poss(pos):
        if pos == "c1":
            return "back"
        if pos == "c2":
            return "left"
        if pos == "c3":
            return "right"
        if pos == "c4":
            return "front"
        if pos == "table":
            return "back"
        if pos == "ontop":
            return "back"
    
    def unique(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]
