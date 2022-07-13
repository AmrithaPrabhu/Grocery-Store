from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = (
        "select product.idproduct, product.productname, product.uom, product.priceperunit, uom.uomname from product inner join uom on product.uom=uom.iduom")
    cursor.execute(query)
    response = []
    for (idproduct, productname, uom, priceperunit, uomname) in cursor:
        response.append({
            'product_id': idproduct,
            'name': productname,
            'uom_id': uom,
            'price_per_unit': priceperunit,
            'uom_name': uomname
        })
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(productname, uom, priceperunit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where idproduct=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


def update_product(connection, product):
    cursor = connection.cursor()
    query = "UPDATE product SET priceperunit=%s WHERE productname=%s"
    data = (product['price_per_unit'],product['product_name'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(update_product(connection, {
        'product_name': "toothpaste",
        'price_per_unit': 50,
    }))
