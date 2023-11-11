from setuptools import setup, find_packages

setup(
    name='compatibilidad',
    version='1.0.0',
    packages=find_packages(),  # Busca automáticamente paquetes en el directorio actual
    # install_requires=[
    #     # Lista de dependencias requeridas por tu paquete
    #     'dependencia1',
    #     'dependencia2',
    # ],
    # entry_points={
    #     'console_scripts' [
    #         'nombre_del_comando = paquete.modulofuncion_principal',
    #     ],
    # },
    author='Candela Lopéz & Naroa Lauzirika',
    author_email='naroa.lauzirika@alumni.mondragon.edu',
    description='Comprabación de la compatibilidad de dos personas',
    long_description='Tiene dos clases, una para amigos y otra para posibles parejas'

)
