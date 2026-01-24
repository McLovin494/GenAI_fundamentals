def update_order():
    chai_type = "elaichi"

    def kitchen():
        # just outside the scope of this
        nonlocal chai_type
        chai_type = "kesar"

    kitchen()
    print(f"After kitchen update {chai_type}")


update_order()
