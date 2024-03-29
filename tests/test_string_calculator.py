from ..src.string_calculator import StringCalculator

def test_add_param_vide_return_zero():
    # arrange
    mon_param = ""
    mon_resultat = 0
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat


def test_add_param_vide_return_meme():
    # arrange
    mon_param = "5"
    mon_resultat = 5
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat

def test_return_somme():
    # arrange
    mon_param = "7;8"
    mon_resultat = 15
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat

def test_wrong_separator_return_zero():
    # arrange
    mon_param = "7,8"
    mon_resultat = 0
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat

def test_wrong_separator_return_sum():
    # arrange
    mon_param = "1001;1000;8;9;1003;4"
    mon_resultat = 21
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat

def test_letter_in_string_return_0():
    # arrange
    mon_param = "1001;1000;8;9;1a003;4"
    mon_resultat = 0
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat

def test_multiply_param_empty_return_zero():
    # arrange
    mon_param = ""
    mon_resultat = 0
    # act
    somme = StringCalculator.multiply(mon_param)
    # assert
    assert somme == mon_resultat

def test_return_multiply():
    # arrange
    mon_param = "7;8"
    mon_resultat = 56
    # act
    produit = StringCalculator.multiply(mon_param)
    # assert
    assert produit == mon_resultat

def test_wrong_separator_return_zero_multiply():
    # arrange
    mon_param = "7,8"
    mon_resultat = 0
    # act
    somme = StringCalculator.multiply(mon_param)
    # assert
    assert somme == mon_resultat

def test_alpha_in_input_return_zero_multiply():
    # arrange
    mon_param = "7;a;3"
    mon_resultat = 21
    # act
    somme = StringCalculator.multiply(mon_param)
    # assert
    assert somme == mon_resultat

def test_number_superior_1000():
    # arrange
    mon_param = "6;1001;2;3000"
    mon_resultat = 12
    # act
    somme = StringCalculator.multiply(mon_param)
    # assert
    assert somme == mon_resultat