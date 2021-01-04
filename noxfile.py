import nox


@nox.session
def bandit(session):
    """ Bandit """
    session.install('.[dev]')
    session.run('bandit', 'mars_insight/')


@nox.session
def coverage(session):
    """ Coverage """
    session.install('.[dev]')
    session.run(
        'pytest',
        '--cov=mars_insight',
        '--cov-report', 'term-missing',
        '--cov-fail-under', '100',
        'tests/',
    )

@nox.session
def doc(session):
    """ Documentation """
    session.install('.[dev]')
    session.run(
        'python', '-m', 'sphinx',
        '-a',
        '-E',
        '-T',
        '-W',
        '-c', 'docs/',
        'docs/',
        'docs/build/',
    )


@nox.session
def flake8(session):
    """ flake8 """
    session.install('.[dev]')
    session.run('flake8', 'mars_insight/')


@nox.session()
def pylint(session):
    """ pylint """
    session.install('.[dev]')
    session.run('pylint', 'mars_insight/')


@nox.session
def pytest(session):
    """ pytest """
    session.install('.[dev]')
    session.run('pytest', 'tests')
