from django.db import models


# Create your models here.

class Categoria_produtos(models.Model):
    nome_categoria = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nome_categoria

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=40)
    qtd_produto = models.IntegerField()
    valor_produto = models.FloatField()
    data_vencimento_produto = models.DateField(auto_now_add=True)
    # img_produto = models.ImageField(upload_to='gerenciador_school/images/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria_produtos,on_delete=models.SET_NULL,null=True)
    # dono = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
                                  
    def __str__(self) -> str:
        return self.nome_produto