from django.db import models

# Create your models here.

class BigCategory(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    def get_latest_post(self):
        result=Post.objects.filter(
            category__parent=self
        ).filter(is_publick=True).order_by('-created_at')[:5]
        return result




class SmallCategory(models.Model):
    name=models.CharField(max_length=200)
    parent=models.ForeignKey(BigCategory,on_delete=models.PROTECT,related_name='parent')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_lateset_post(self):
        result=Post.objects.filter(
            category=self
        ).filter(
            is_publick=True
        ).order_by('-created_at')[:5]

        return result


class Tag(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def get_latest_post(self):
        result=Post.objects.filter(
            tag=self
        ).filter(
            is_publick=True
        ).order_by('-created_at')[:5]
        return result

class BlogBlock(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()


    def __str__(self):
        return self.title


class Post(models.Model):
    bigtitle=models.CharField(max_length=255)
    bigtext=models.TextField()
    smallblog=models.ManyToManyField(BlogBlock,blank=False)
    category=models.ForeignKey(SmallCategory,on_delete=models.PROTECT,related_name='small_category')
    tag=models.ManyToManyField(Tag,blank=False)
    thumnail=models.ImageField(upload_to='images/', null=True, blank=True)
    is_publick=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bigtitle





class Comment(models.Model):
    name=models.CharField(max_length=200)
    text=models.TextField()
    target=models.ForeignKey(Post,on_delete=models.PROTECT,related_name='target')
    created_at=models.DateTimeField(auto_now_add=True)
    is_public=models.BooleanField(default=False)

    def __str__(self):
        return self.text[:10]


class Reply(models.Model):
    name=models.CharField(max_length=255,blank=True)
    text=models.TextField()
    target=models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_public=models.BooleanField(default=False)


    def __str__(self):
        return  self.name
