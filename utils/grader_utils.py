import os
import subprocess
from requests import post
import pickle

class Grader:
    def __init__(self, section_id, user_email, n_tasks=0, tests_path: str = None, code_file: str = None):
        self.post_data = {'section_id': section_id,
                          'user_email': user_email,
                          'n_tasks': int(n_tasks)}
                          
        self.tests_path = tests_path
        self.code_file = code_file
        
    def run_code(self, code_file: str, input: str):
        result = subprocess.run(['python', code_file], 
                            input=bytes(input, 'utf-8'),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        
        return result.stdout, result.stderr
       
    def add_task(self, task_id, output):
        self.post_data[task_id] = output
        
    def grade_code(self):
        outputs = []
        for file in sorted(os.listdir(self.tests_path)):
            if 'test' in file:
                with open(self.tests_path+'/'+file, 'r') as f:
                    inp = f.read()
                    
                out, err = self.run_code(self.tests_path+'/'+self.code_file, inp)
                
                outputs.append(out)
                
        self.post_data['n_tasks'] = len(outputs)
        for i, out in enumerate(outputs):
            self.add_task(f"t{i+1}", out.decode('utf-8').strip())
    
        self.grade()
        
    def eval_func(self, tests_file, func):
        error = False
        res = []
        with open(tests_file, 'rb') as f:
            while True:
                try:
                    res.append(func(pickle.load(f)))
                except EOFError:
                    break
        
        i = len(self.post_data) - 3
        for val in res:
            self.add_task(f"t{i+1}", str(val))
            i += 1
            
        self.post_data['n_tasks'] = len(self.post_data) - 3
    
        
    def grade(self):
        response = post('https://python-course.herokuapp.com/grader', json=self.post_data)
        
        msg = eval(response.content)['msg']
        
        print(msg)


if __name__ == '__main__':
    grader = Grader(section_id="gF0xtYCkloKux5W9MgBY", user_email="rvillcap@fcpn.edu.bo", n_tasks="3")

    grader.add_task("t1", "hola")
    grader.add_task("t2", "como")
    grader.add_task("t3", "estas")

    grader.grade()

