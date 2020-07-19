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
        '-a', # Update all output files
        '-E', # Do not reuse environment from previous run
        '-T', # Show full trace on error
        '-W', # Treat warnings as errors
        '-c', 'docs/',
        'docs/src/',
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