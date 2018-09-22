import jinja2
import json
import os


def generate_problems():
    output_directory = "_output"
    data_directory = "_data"

    # we will make sure that the output directory exists
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    f = open(os.path.join(output_directory, "problems.txt"), "w")
    problem=1

    for i in range(1,3):

        template_file = os.path.join(data_directory,"problem"+str(i)+".j2")
        #template_file = "_data/problem1.j2"
        json_parameter_file = \
            os.path.join(data_directory, "parameters"+str(i)+".json")
        #json_parameter_file = "_data/parameters1.json"

        # read the contents from the JSON files
        print("Read JSON parameter file...%s" % json_parameter_file)
        config_parameters = json.load(open(json_parameter_file))

        # next we need to create the central Jinja2 environment and we will load
        # the Jinja2 template file (the two parameters ensure a clean output in the
        # configuration file)
        print("Create Jinja2 environment using template %s" % template_file)
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                            trim_blocks=True,
                            lstrip_blocks=True)
        template = env.get_template(template_file)

        # now create the templates
        print("Create templates...")
        for parameter in config_parameters:
            result = template.render(parameter)
            f.write("\n\nProblem : %d\n" % problem)
            f.write(result)
            problem+=1

    print("File '%s' created..." % "problems.txt")
    print("DONE")
    f.close()


def main():
    generate_problems()

if __name__ == '__main__':
    main()
