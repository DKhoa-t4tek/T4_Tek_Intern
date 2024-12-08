from utils import shared_function

def identify_elememts_commas(special_elements_list):

    address = None
    area = None
    num_floors = None
    num_rooms = None
    price = None
    unit = None
    position = None
    name_hd = None
    nphn = None

    ty_index = special_elements_list.index('tỷ') if 'tỷ' in special_elements_list else None
    hd_index = special_elements_list.index('HĐ') if 'HĐ' in special_elements_list else None
    nphn_index = next((i for i, element in enumerate(special_elements_list) if element.startswith('NPHN')), None)


     # Get NPHN index
    if nphn_index is not None:
        nphn = special_elements_list[nphn_index].replace(',', '')

    if ty_index is not None:

        # address, price, unit, num_floor, nums_rooms
        area, num_floors, num_rooms, price, unit = shared_function.identify_elements_after_ty(special_elements_list, ty_index)

        area_index = len(special_elements_list) - 1 - special_elements_list[::-1].index(special_elements_list[ty_index - 4])

        # Xử lý trường hợp area_index trùng với ty_index
        if area_index == ty_index:
            area_index = len(special_elements_list) - 1 - special_elements_list[::-1].index(special_elements_list[ty_index - 4])
   
        address = ' '.join(special_elements_list[:area_index])

        if hd_index is not None:
            position = special_elements_list[hd_index + 1]
            position_index = special_elements_list.index(position)

            # If there's not elements in front of "HĐ" element, the elements assign is None
            if hd_index == 0:
                address = None
                area = None
                num_floors = None
                num_rooms = None
                price = None
                unit = None

            if nphn_index is not None:
                name_hd = ' '.join(special_elements_list[position_index+1:nphn_index])
            else:
                name_hd = ' '.join(special_elements_list[position_index+1:])
        else:
            pass

    return [address, str(area), num_floors, num_rooms, price, unit, position, name_hd, nphn]










    