from unittest.mock import Mock
import pytest
from sqlalchemy.orm import joinedload, Session
from servise import FilialsServise,FilialsModel


@pytest.fixture
def mock_sess(mock):
    mock_sess = Mock(spec=Session, autospec = True)
    mock.patch('database.session',return_value = mock_sess)
    return mock_sess



def test_get_all_filial():
    mock_fil = FilialsModel(filial = 'qwe')
    mock_sess.execute.return_value.scalars.return_value.all.return_value = [mock_fil]
    result = FilialsServise.get_all()

    assert len(result) == 1
    assert result[0].filial == 'qwe'
    assert result[0].id == 1
    assert result[0].isative == True
    mock_sess.execute.assert_called_once()
    


