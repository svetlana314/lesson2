def discounted(price, discount, max_discount=20):
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    
if __name__ == "__main__":
    try:
        print(discounted('ss',10))    
    except ValueError:
        print('Введены некорректные данные')