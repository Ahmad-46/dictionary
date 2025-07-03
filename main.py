student_data = {'id1':
    {'name' : ['hani'],
     'class': ['VII'],
     'subject_integration': ['coding, math, science']
     },
    'id2':
        {'name' : ['Ahmad'],
         'class' : ['IX'],
          'subject_integration' : ['coding, physics, computer'],
          },
        'id3':
           {'name' : ['hani'],
            'class': ['VII'],
            'subject_integration': ['coding, math, science']
            },
           'id4':
               {'name' : ['abdul'],
                'class': ['IX'],
                'subject_integration': ['coding, math, science']
        },
}


result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        
print(result)        