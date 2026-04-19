import os

def plan(plan):
    try:
        directory = os.path.dirname(os.path.abspath("./plan.md"))
        if directory:
            os.makedirs(directory, exist_ok=True)
            
        with open("./plan.md", 'w', encoding='utf-8') as f:
            f.write(plan)
            
        return f"Success: Created plan.md at {directory}."
    except Exception as e:
        return f"Error creating plan.md in {directory}: {str(e)}"