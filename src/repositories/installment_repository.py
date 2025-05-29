from repositories.sqlalchemy.mappers.installment_mapper import InstallmentMapper

class InstallmentRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, installment):
        with self.session_factory() as session:
            model = InstallmentMapper.to_model(installment)
            session.add(model)
            session.commit()
            session.refresh(model)
            
            return InstallmentMapper.to_domain(model)
        
    def add_many(self, installments):
        for installment in installments:
            self.add(installment)