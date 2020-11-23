import pytest

l = ['a', 'b', 'c']
text1 = ('William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.')
n = []
t = 0
n1 =[]

class TestClass:



    #проверяем длину списка
    @pytest.fixture(scope="function")
    def test_one(self):
        assert len(l) == 3

    #подсчитывает общее количество артиклей: 'a', 'an', 'the'
    def test_text(self):
        for i in text1:
            n.append(i)
        cnt1 = n.count('a')
        cnt2 = n.count('an')
        cnt3 = n.count('the')
        print('Общее количество артиклей:', cnt1 + cnt2 + cnt3)

    #Пишем программу, которая меняет местами минимальный и максимальный элемент этого списка.
    def test_num(self):
        s = ('10 9 8 7 6 5 4 3 2 1').split()
        for i in s:
            t = int(i)
            n1.append(t)

        minimum = n1.index(min(n1))
        maximum = n1.index(max(n1))
        n1[minimum], n1[maximum] = max(n1), min(n1)
        print(*n1)

    def test_full_list(self):
        numbers = [8, 9, 10, 11]

        numbers[1] = 17    #Заменил второй элемент списка на 17
        numbers.extend([4, 5, 6])    #Добавил числа 4, 5 и 6 в конец списка;
        del numbers[0]    #Удалил первый элемент списка;
        numbers *= 2    #Удвоил список
        numbers.insert(3, 25)    #Вставил число 25 по индексу 3
        print(numbers)

@pytest.fixture(scope="function")
def setup_function_fixture():
    print("\nstart browser for test..")
    yield
    print("\nquit browser..")