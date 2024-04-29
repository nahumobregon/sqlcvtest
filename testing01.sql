-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[testing01] AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	-- se agregan cambios para una tercer prueba

	-- CAmbios realizados 
	declare @Param1 varchar(2) = 'ae'

    -- Insert statements for procedure here
	SELECT @Param1

	-- Se agregan estos cambios
	-- para probar si funciona el control de cambios
	-- en GIT

	-- Se agregan cambios para una segunda prueba
END
