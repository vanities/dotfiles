Vim�UnDo� �H�d�9ܟEsG��n�7��ζ���[�0l   ;   1        BlogPost = apps.get_model("blog", "Post")   0   &                       ]�W�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�W�    �               "   from django.apps import apps    from django.test import TestCase   ;from django.db.migrations.executor import MigrationExecutor    from django.db import connection           class TestMigrations(TestCase):           @property       def app(self):   I        return apps.get_containing_app_config(type(self).__module__).name           migrate_from = None       migrate_to = None           def setUp(self):   7        assert self.migrate_from and self.migrate_to, \   n            "TestCase '{}' must define migrate_from and migrate_to     properties".format(type(self).__name__)   ;        self.migrate_from = [(self.app, self.migrate_from)]   7        self.migrate_to = [(self.app, self.migrate_to)]   0        executor = MigrationExecutor(connection)   H        old_apps = executor.loader.project_state(self.migrate_from).apps       +        # Reverse to the original migration   +        executor.migrate(self.migrate_from)       +        self.setUpBeforeMigration(old_apps)       #        # Run the migration to test   0        executor = MigrationExecutor(connection)   0        executor.loader.build_graph()  # reload.   )        executor.migrate(self.migrate_to)       G        self.apps = executor.loader.project_state(self.migrate_to).apps5�_�                    $   +    ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �   %            �   %            �   $            5�_�                    &        ����                                                                                                                                                                                                                                                                                                                                                             ]�W�    �               )   from django.apps import apps    from django.test import TestCase   ;from django.db.migrations.executor import MigrationExecutor    from django.db import connection           class TestMigrations(TestCase):       @property       def app(self):   I        return apps.get_containing_app_config(type(self).__module__).name           migrate_from = None       migrate_to = None           def setUp(self):           assert (   1            self.migrate_from and self.migrate_to   Y        ), "TestCase '{}' must define migrate_from and migrate_to     properties".format(               type(self).__name__   	        )   ;        self.migrate_from = [(self.app, self.migrate_from)]   7        self.migrate_to = [(self.app, self.migrate_to)]   0        executor = MigrationExecutor(connection)   H        old_apps = executor.loader.project_state(self.migrate_from).apps       +        # Reverse to the original migration   +        executor.migrate(self.migrate_from)       +        self.setUpBeforeMigration(old_apps)       #        # Run the migration to test   0        executor = MigrationExecutor(connection)   0        executor.loader.build_graph()  # reload.   )        executor.migrate(self.migrate_to)       G        self.apps = executor.loader.project_state(self.migrate_to).apps           )    def setUpBeforeMigration(self, apps):           pass    5�_�                    '        ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �   (               �   )            �   '                  �   '            5�_�                    )        ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �   (   *   <      "lass TagsTestCase(TestMigrations):5�_�      	              )        ����                                                                                                                                                                                                                                                                                                                                                             ]�W�    �               <   from django.apps import apps    from django.test import TestCase   ;from django.db.migrations.executor import MigrationExecutor    from django.db import connection           class TestMigrations(TestCase):       @property       def app(self):   I        return apps.get_containing_app_config(type(self).__module__).name           migrate_from = None       migrate_to = None           def setUp(self):           assert (   1            self.migrate_from and self.migrate_to   Y        ), "TestCase '{}' must define migrate_from and migrate_to     properties".format(               type(self).__name__   	        )   ;        self.migrate_from = [(self.app, self.migrate_from)]   7        self.migrate_to = [(self.app, self.migrate_to)]   0        executor = MigrationExecutor(connection)   H        old_apps = executor.loader.project_state(self.migrate_from).apps       +        # Reverse to the original migration   +        executor.migrate(self.migrate_from)       +        self.setUpBeforeMigration(old_apps)       #        # Run the migration to test   0        executor = MigrationExecutor(connection)   0        executor.loader.build_graph()  # reload.   )        executor.migrate(self.migrate_to)       G        self.apps = executor.loader.project_state(self.migrate_to).apps       )    def setUpBeforeMigration(self, apps):           pass       #class TagsTestCase(TestMigrations):       ,    migrate_from = '0009_previous_migration'   .    migrate_to = '0010_migration_being_tested'       )    def setUpBeforeMigration(self, apps):   1        BlogPost = apps.get_model('blog', 'Post')   /        self.post_id = BlogPost.objects.create(   ,            title = "A test post with tags",               body = "",               tags = "tag1 tag2",           ).id       !    def test_tags_migrated(self):   6        BlogPost = self.apps.get_model('blog', 'Post')   4        post = BlogPost.objects.get(id=self.post_id)       .        self.assertEqual(post.tags.count(), 2)   9        self.assertEqual(post.tags.all()[0].name, "tag1")   9        self.assertEqual(post.tags.all()[1].name, "tag2")5�_�      
           	      F    ����                                                                                                                                                                                                                                                                                                                                                             ]�W�    �         ;      Y        ), "TestCase '{}' must define migrate_from and migrate_to     properties".format(5�_�   	              
   0   &    ����                                                                                                                                                                                                                                                                                                                                                             ]�W�     �   /   1   ;      1        BlogPost = apps.get_model("blog", "Post")5�_�   
                  0   (    ����                                                                                                                                                                                                                                                                                                                                                             ]�W�    �   /   1   ;      2        BlogPost = apps.get_model("blolg", "Post")5��