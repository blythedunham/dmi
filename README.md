# Django Model Inheritance (DMI) Examples

Here lies the example models used in the [Ins & Outs of Models Inheritance (slides)](./TheInsAndOutsOfModelInheritance.pdf) presented at [DjangoCon 2019](https://2019.djangocon.us/talks/the-ins-and-outs-of-model-inheritance/). In some cases, the  names have been changed to protect the innocent models from redundancy.


### Exploring the Models
1. Migrate to create tables:
```
python3 manage migrate
```

2. Run `shell` or `shell_plus`
This project includes [django-extensions](https://github.com/django-extensions/django-extensions) so you use shell plus and print all the SQL executed with `--print-sql`.

```
python3 manage shell_plus --print-sql
```

Example with Multi-Table Inheritance
```
from mti.models import BigCat  # shell_plus auto imports
from mti.models import Cheetah
from mti.models import Lion

Lion.objects.create(name='Simba', giraffes_hunted=0)
Cheetah.objects.create(name='Chester')
cats = BigCat.objects.all()
cats[0].lion.name
```

3. The database is sqlite for convenience. To query the command line:

```
python3 manage dbshell
```

```
sqlite> .tables
abstract_giraffe            django_migrations
abstract_zebra              django_session
auth_group                  gfk_blog
auth_group_permissions      gfk_comment
auth_permission             mti_bigcat
auth_user                   mti_cheetah
auth_user_groups            mti_lion
auth_user_user_permissions  polymorph_artproject
basic_leg                   polymorph_project
basic_snowgiraffe           polymorph_researchproject
basic_tongue                proxy_person
django_admin_log            sti_vehicle
django_content_type         tmodels_typedanimal
sqlite> .schema basic_snowgiraffe
CREATE TABLE IF NOT EXISTS "basic_snowgiraffe" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL);
```
