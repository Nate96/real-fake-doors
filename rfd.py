import click
import RealFakeDoors


@click.command()
@click.option('--run', '-r',
              type=str,
              required=False,
              default='test',
              help='run given script')
@click.option('--database', '-d',
              type=str,
              required=False,
              default='users',
              help='connect to geven database')
@click.option('--cvs',
              type=str,
              required=False,
              default='index',
              help='import data from a given csv')
def rfd(run, database, csv):
    RealFakeDoors.run_sql_script(run, database)


if __name__ == '__main__':
    rfd()
