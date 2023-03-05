from django import forms


class LoginForms(forms.Form):
    email=forms.EmailField(
        max_length=100,
        required=True,
        label="E-mail do Usuário",
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: kmbappe@xpto.com",
            },
        )
    )
    senha=forms.CharField(
        max_length=70,
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_usuario=forms.CharField(
        max_length=100,
        required=True,
        label="Nome do Usuário",
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Kilian Mbappé",
            },
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: kmbappe@xpto.com",
            },
        )
    )
    senha_1=forms.CharField(
        max_length=70,
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        max_length=70,
        required=True,
        label="Confirmação de senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme sua senha"
            }
        )
    )
